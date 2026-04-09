# Standard Library Test Suite

This directory contains conformance tests for Python's standard library modules.
Tests validate that Python implementations conform to the language reference specification
for standard library functionality.

## Testing Methodology

Each test module follows this dual-validation approach:

1. **AST-Based Validation (50%)**
   - Validates syntax and structure against reference
   - Ensures correct import statements and module organization
   - Checks for reserved keyword usage

2. **Runtime Behavior Verification (30%)**
   - Tests basic functionality works as expected
   - Validates type signatures and return values
   - Checks error handling and edge cases

3. **Implementation Compatibility (20%)**
   - Verifies behavior matches CPython reference
   - Tests cross-platform behavior
   - Validates interoperability with core language features

## Targeted Modules

### Tier 1: Core Modules (Priority: High)

Core modules essential for fundamental Python functionality.

- `types` - Core type objects and metaclasses
- `itertools` - Functional tool iterators
- `functools` - Higher-order functions and decorators
- `collections` - Container datatypes
- `math` - Mathematical functions
- `random` - Random number generation
- `datetime` - Date and time handling
- `re` - Regular expressions
- `json` - JSON encoding/decoding
- `io` - In-memory and filesystem I/O
- `os` - Operating system interfaces
- `pathlib` - Object-oriented filesystem paths

### Tier 2: High-Utility Modules (Priority: Medium)

Commonly used modules for everyday programming tasks.

- `csv` - CSV file processing
- `typing` - Type hints and generic types
- `hashlib` - Secure hash algorithms
- `secrets` - Cryptographically strong random numbers
- `time` - Time access and conversions
- `statistics` - Statistical functions
- `http.client` - HTTP client protocol
- `urllib.parse` - URL parsing and manipulation
- `copy` - Object copying operations
- `pickle` - Python object serialization
- `shelve` - Persistent key-value store
- `marshal` - Internal Python object serialization
- `decimal` - Decimal floating point arithmetic
- `fractions` - Rational numbers
- `cmath` - Complex mathematical functions

### Tier 3: Advanced Modules (Priority: Low)

Specialized modules for advanced use cases.

- `asyncio` - Asynchronous I/O
- `multiprocessing` - Multi-process programming
- `threading` - Multi-threading
- `subprocess` - Process spawning and management
- `sqlite3` - SQLite database access
- `dbm` - Interface to Unix database files
- `ctypes` - Foreign function calls
- `shelve` (duplicate) - Persistent key-value store

## Coverage Metrics

**Overall Target:** 70%+ module coverage

- **Tier 1:** 90%+ module coverage (all critical paths tested)
- **Tier 2:** 75%+ module coverage (most common functions tested)
- **Tier 3:** 50%+ module coverage (core functionality tested)

Module-level coverage metrics will be tracked in each module's test file using pytest markers.

## Test Structure

```
tests/stdlib/
├── __init__.py          # Module initialization
├── README.md            # This file
├── docs/                # Module specification documents
│   └── [module_name].md
└── [module_name]/       # Module-specific test files
    ├── __init__.py
    └── test_module.py
```

Each module has its own directory following the naming convention:
`test_<module_name>.py`

## Running Tests

```bash
# Run all stdlib tests
pytest tests/stdlib/

# Run specific module tests
pytest tests/stdlib/test_types.py

# Run tests with verbose output
pytest tests/stdlib/ -v

# Run tests excluding specific modules
pytest tests/stdlib/ --ignore=tests/stdlib/test_asyncio.py
```

## Reference Implementation

The test suite is designed to validate conformance across different Python implementations.
When differences are observed, they should be documented in the module's test file or in
`tests/stdlib/docs/differences.md`.

## Maintenance

- **Weekly:** Review failing tests and update test cases
- **Monthly:** Update module documentation and add new test coverage
- **Quarterly:** Audit coverage metrics and adjust module priorities

## Related Issues

- Issue #1: Add standard library check
- Issue #3: Directory structure + base README
- Issue #4: Base `StdlibModuleTester` test class
- Issue #5-7: Module-specific implementation issues
- Issue #8: GitHub Actions CI workflow
- Issue #9: Standard maintenance procedures

See [DESIGN-ADD-STANDARD-LIBRARY-COVERAGE.md](../../DESIGN-ADD-STANDARD-LIBRARY-COVERAGE.md) for full design details.