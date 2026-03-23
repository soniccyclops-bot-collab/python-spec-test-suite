# Python Language Reference Conformance Test Suite

A comprehensive test suite that validates Python implementation conformance to the official [Python Language Reference](https://docs.python.org/3/reference/).

## 🎯 Goal

Convert the prose-based Python Language Reference into executable conformance tests that verify any Python implementation (CPython, PyPy, Jython, etc.) meets the specification requirements.

## 🔧 Quick Start

```bash
# Setup
make setup

# Run Section 2.6 proof of concept  
make test-section SECTION=2.6

# Check for new PEPs to process
make check-peps

# Full weekly maintenance cycle
make weekly-check
```

## 📋 Current Status

### ✅ Completed
- **Section 2.6 Numeric Literals**: Complete conformance test suite with 100% grammar coverage
- **Utility Scripts**: PEP monitoring, parsing, and test generation tools
- **Makefile Automation**: Build targets for all common workflows
- **Test Framework**: AST-based parsing validation with cross-implementation support

### 🚧 In Progress  
- Section 2.7 Operators and Delimiters
- Automated PEP integration pipeline
- Cross-implementation validation results

### 📅 Planned
- Complete Section 2 (Lexical Analysis) coverage
- Section 6 (Expressions) conformance tests
- Section 7-8 (Statements) validation
- Integration with Python development workflow

## 🏗️ Architecture

```
python-spec-test-suite/
├── tests/conformance/          # Generated conformance tests
│   ├── section_2_6_numeric_literals.py
│   └── SECTION_2_6_DOCUMENTATION.md  
├── scripts/                    # Utility automation
│   ├── fetch_new_peps.py      # PEP monitoring
│   ├── parse_pep_changes.py   # Language Reference change detection
│   ├── format_for_ai.py       # AI prompt generation
│   └── run_conformance_tests.py
├── data/                       # Generated data and caches
│   ├── last_check.json        # PEP processing state
│   ├── pep_cache/             # Downloaded PEP content
│   └── results/               # Test execution results
├── Makefile                   # Build automation
└── requirements.txt           # Python dependencies
```

## 📊 Test Coverage: Section 2.6 Numeric Literals

**Grammar Coverage: 100%**
- ✅ Integer literals (decimal, binary, octal, hex)
- ✅ Floating-point literals (all component variations)  
- ✅ Imaginary literals (j/J suffix with all base types)
- ✅ Underscore grouping rules and restrictions

**Prose Requirements: 100%**  
- ✅ Leading zero restrictions ("not allowed in non-zero decimal")
- ✅ Underscore placement rules ("can only occur between digits")
- ✅ Base prefix validation (0b/0B, 0o/0O, 0x/0X)
- ✅ Case sensitivity specifications
- ✅ Error condition requirements

**Test Types:**
- **92 positive tests** - Valid syntax that should parse correctly
- **38 negative tests** - Invalid syntax that should raise SyntaxError  
- **12 edge cases** - Implementation limits and boundary conditions
- **8 cross-implementation** - Compatibility validation tests

## 🤖 AI-Assisted Maintenance

This repository is designed for **AI-driven maintenance** via weekly heartbeat processing:

### Weekly Workflow
1. **Monitor**: `make check-peps` - Detect new Language Reference changes
2. **Process**: `make process-new-peps` - Parse PEP modifications  
3. **Generate**: AI creates conformance tests from structured prompts
4. **Validate**: `make test` - Verify generated tests work correctly
5. **Commit**: Push new tests to repository

### Human Oversight
- **Trigger**: Human schedules weekly processing (no autonomous operation)
- **Review**: Generated tests committed for human review before merging
- **Quality**: AI follows established patterns from Section 2.6 implementation

## 🔍 Test Methodology

### AST-Based Validation
```python
def parse_literal(self, literal: str) -> Union[int, float, complex]:
    tree = ast.parse(literal, mode='eval')
    return tree.body.value
```

**Benefits:**
- **Security**: No `eval()` usage, only parsing validation
- **Precision**: Tests literal parsing, not runtime evaluation  
- **Cross-implementation**: Works consistently across Python implementations

### Specification Mapping
Every test directly maps to Language Reference requirements:

```python
def test_leading_zeros_forbidden(self, tester):
    """Test: 'Leading zeros in a non-zero decimal number are not allowed'"""
    tester.assert_syntax_error("0123")  # Direct Language Reference quote
```

## 🚀 Usage Examples

### Development Testing
```bash
# Test current implementation
make test

# Test specific grammar area  
make test-section SECTION=2.6

# Cross-implementation validation
python3.10 -m pytest tests/conformance/section_2_6_numeric_literals.py
pypy3 -m pytest tests/conformance/section_2_6_numeric_literals.py
```

### CI/CD Integration
```yaml
- name: Validate Language Reference Conformance
  run: |
    make test
    make benchmark
```

### Implementation Development
```bash
# Check what's changed recently
make check-peps

# Process specific PEP
make process-pep PEP=701

# Generate tests for PEP changes
make generate-tests PEP=701
```

## 📈 Project Vision

**Year 1**: Complete lexical analysis conformance (Sections 2-3)
**Year 2**: Expression and statement validation (Sections 6-8)  
**Year 3**: Full Language Reference coverage
**Year 5**: Standard conformance baseline for all Python implementations

### Success Metrics
- **Adoption**: All major Python implementations use for conformance validation
- **Integration**: Part of standard Python development workflow  
- **Quality**: Catches real specification compliance differences
- **Maintenance**: Fully automated via AI-assisted weekly updates

## 🤝 Contributing

This project uses **AI-first development**:

1. **Structured Input**: PEPs and Language Reference changes → formatted prompts
2. **AI Generation**: Comprehensive test suites following established patterns
3. **Human Review**: Quality validation and integration oversight
4. **Automated Maintenance**: Self-updating via scheduled processing

For questions or suggestions, see the [project issues](https://github.com/soniccyclops-bot-collab/python-spec-test-suite/issues).

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

---

*Building the definitive Python specification conformance test suite, one section at a time.*