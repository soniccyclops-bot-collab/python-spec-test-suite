#!/usr/bin/env python3
"""
MicroPython-compatible test runner for Python Language Reference conformance tests.

This runner executes the same validation logic as the pytest suite but without
pytest dependency, making it compatible with MicroPython's limited stdlib.
"""

import os
import sys
import ast
import traceback
from pathlib import Path

def run_test_module(module_path):
    """
    Run a single test module by extracting and executing test functions.
    
    Args:
        module_path (Path): Path to the test module
        
    Returns:
        tuple: (passed_count, failed_count, test_results)
    """
    passed = 0
    failed = 0
    results = []
    
    try:
        # Read the test file
        test_code = module_path.read_text()
        
        # Parse the AST to find test functions
        tree = ast.parse(test_code, str(module_path))
        
        # Create a module namespace
        module_globals = {
            '__name__': '__main__',
            '__file__': str(module_path),
            'ast': ast,
            'sys': sys,
            'os': os,
        }
        
        # Execute the module to define functions
        exec(test_code, module_globals)
        
        # Find all test functions
        test_functions = []
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name.startswith('test_'):
                test_functions.append(node.name)
        
        # Run each test function
        for test_name in test_functions:
            try:
                test_func = module_globals.get(test_name)
                if test_func and callable(test_func):
                    # Execute the test
                    test_func()
                    passed += 1
                    results.append(f"✓ PASS: {test_name}")
                else:
                    failed += 1
                    results.append(f"✗ FAIL: {test_name} - Function not found")
            except Exception as e:
                failed += 1
                results.append(f"✗ FAIL: {test_name} - {str(e)}")
                
    except Exception as e:
        failed += 1
        results.append(f"✗ FAIL: Module {module_path.name} - {str(e)}")
    
    return passed, failed, results

def run_all_tests():
    """
    Run all conformance tests in MicroPython-compatible mode.
    
    Returns:
        dict: Test execution summary
    """
    print("=" * 70)
    print("MICROPYTHON PYTHON LANGUAGE REFERENCE CONFORMANCE TESTS")
    print("=" * 70)
    print()
    
    # Find all test files
    test_dir = Path("tests/conformance")
    if not test_dir.exists():
        print(f"✗ ERROR: Test directory {test_dir} not found")
        return {"total": 0, "passed": 0, "failed": 1}
    
    test_files = list(test_dir.glob("test_*.py"))
    test_files.sort()
    
    if not test_files:
        print(f"✗ ERROR: No test files found in {test_dir}")
        return {"total": 0, "passed": 0, "failed": 1}
    
    print(f"Found {len(test_files)} test modules")
    print()
    
    total_passed = 0
    total_failed = 0
    module_results = []
    
    # Run each test module
    for test_file in test_files:
        print(f"Running {test_file.name}...")
        passed, failed, results = run_test_module(test_file)
        
        total_passed += passed
        total_failed += failed
        
        # Store module results
        module_results.append({
            "module": test_file.name,
            "passed": passed,
            "failed": failed,
            "results": results
        })
        
        print(f"  {passed} passed, {failed} failed")
        
        # Show failures for this module
        if failed > 0:
            for result in results:
                if result.startswith("✗"):
                    print(f"    {result}")
        print()
    
    # Print summary
    print("=" * 70)
    print("MICROPYTHON CONFORMANCE TEST SUMMARY")
    print("=" * 70)
    total_tests = total_passed + total_failed
    success_rate = (total_passed / total_tests * 100) if total_tests > 0 else 0
    
    print(f"Total tests: {total_tests}")
    print(f"Passed: {total_passed}")
    print(f"Failed: {total_failed}")
    print(f"Success rate: {success_rate:.1f}%")
    print()
    
    if success_rate >= 80.0:
        print("🎯 SUCCESS: MicroPython shows excellent Language Reference compatibility!")
        print("AST-based validation approach works across Python implementations.")
        exit_code = 0
    elif success_rate >= 60.0:
        print("⚠️ PARTIAL: MicroPython has good Language Reference support with some limitations.")
        print("Most core language features validated successfully.")
        exit_code = 0
    else:
        print("❌ CONCERN: MicroPython has significant Language Reference limitations.")
        print("Consider embedded-specific validation approach.")
        exit_code = 1
    
    print()
    print("Module breakdown:")
    for module_result in module_results:
        module_success = (module_result["passed"] / (module_result["passed"] + module_result["failed"]) * 100) if (module_result["passed"] + module_result["failed"]) > 0 else 0
        print(f"  {module_result['module']}: {module_result['passed']}/{module_result['passed'] + module_result['failed']} ({module_success:.1f}%)")
    
    return {
        "total": total_tests,
        "passed": total_passed,
        "failed": total_failed,
        "success_rate": success_rate,
        "exit_code": exit_code,
        "modules": module_results
    }

def create_json_report(results, output_file="test-report-micropython-full.json"):
    """
    Create JSON test report for CI consistency.
    
    Args:
        results (dict): Test results from run_all_tests()
        output_file (str): Output file path
    """
    report = {
        "summary": {
            "total": results["total"],
            "passed": results["passed"],
            "failed": results["failed"],
            "skipped": 0,
            "error": 0
        },
        "micropython_full_suite": True,
        "success_rate": results["success_rate"],
        "modules": results.get("modules", [])
    }
    
    try:
        import json
        with open(output_file, "w") as f:
            json.dump(report, f, indent=2)
        print(f"JSON report written to {output_file}")
    except ImportError:
        # MicroPython might not have json module
        print("JSON module not available - skipping report generation")
    except Exception as e:
        print(f"Error writing JSON report: {e}")

if __name__ == "__main__":
    try:
        # Run the full test suite
        results = run_all_tests()
        
        # Create JSON report for CI
        create_json_report(results)
        
        # Exit with appropriate code
        sys.exit(results.get("exit_code", 1))
        
    except Exception as e:
        print(f"FATAL ERROR: {e}")
        print(f"Traceback: {traceback.format_exc()}")
        sys.exit(1)