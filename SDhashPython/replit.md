# SDhash Python Wrapper Project

## Overview
This project contains the SDhash Python wrapper (`jc_sdhash`), which provides a simple, functional API for the SDHash binary. SDHash is a similarity-preserving hash function useful for forensic analysis and file comparison.

## Current Status
- ✅ Repository cloned and set up successfully
- ✅ Python 3.11 environment configured
- ✅ Missing system dependencies (libgomp) resolved
- ✅ Package installed in development mode
- ✅ All core functionality tested and working
- ✅ Interactive demo created and configured as workflow

## Project Architecture
- **Main Package**: `jc_sdhash/` - Contains the Python wrapper for SDHash
  - `__init__.py` - Package initialization and exports
  - `wrapper.py` - Core wrapper functionality
  - `sdhash` - SDHash binary executable (Linux x64)
- **Demo**: `demo.py` - Interactive demonstration of all features
- **Tests**: `test_sdhash.py` - Basic functionality tests

## Recent Changes (September 6, 2025)
- Resolved SDHash binary dependency issues by installing gcc-unwrapped for libgomp
- Created comprehensive demo script with all functionality examples
- Set up workflow to run interactive demo
- Configured proper .gitignore for Python project

## Functionality Verified
1. **Hash Generation**: Generate SDBF hashes from files ✅
2. **Hash Saving**: Save hashes to output files ✅
3. **Hash Comparison**: Compare similarity between SDBF files ✅
4. **Hash Validation**: Validate SDBF file integrity ✅

## Usage Examples
```python
import jc_sdhash as sd

# Generate hash
hash_result = sd.generate("file.txt")

# Save hash to file
sd.generate("file.txt", output_filepath="output")

# Compare hashes
similarity = sd.compare("hash1.sdbf", "hash2.sdbf")

# Validate hash file
validation = sd.validate("hash.sdbf")
```

## System Requirements
- Linux-based OS (verified working on Replit NixOS)
- Python 3.6+
- libgomp (OpenMP library) - installed via gcc-unwrapped
- SDHash binary (included in package)

## Notes
- The SDHash binary automatically appends `.sdbf` extension to output files
- Package works only on Linux (x64 architecture)
- All dependencies resolved and package fully functional