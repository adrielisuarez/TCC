# Overview

TLSH (Trend Micro Locality Sensitive Hash) is a fuzzy matching library that generates locality-sensitive hashes for similarity comparison. The library can detect similar content by comparing hash values, making it particularly useful for malware analysis, file deduplication, and content similarity detection. TLSH requires a minimum of 50 bytes of input data with sufficient complexity to generate meaningful hash values.

# User Preferences

Preferred communication style: Simple, everyday language.

# System Architecture

## Core Library Design
- **Language**: Primarily C++ implementation with extensive multi-language bindings
- **Build System**: CMake-based build configuration with support for multiple platforms (Linux, Windows, macOS)
- **Library Structure**: Static library compilation with configurable bucket sizes (128/256) and checksum lengths (1/3 bytes)

## Hash Algorithm Configuration
- **Bucket Configuration**: Configurable between 128 and 256 buckets via `TLSH_BUCKETS_128` and `TLSH_BUCKETS_256` compile-time options
- **Checksum Options**: Selectable 1-byte or 3-byte checksums via `TLSH_CHECKSUM_1B` compile-time flags
- **Version Compatibility**: Supports both legacy 70-character hashes and newer T1-prefixed format for backward compatibility

## Multi-Language Support
- **Python Extension**: Native C++ extension with pip-installable package (`py-tlsh`)
- **Java Implementation**: Complete Java port with Gradle build system and Maven compatibility
- **JavaScript/Web**: Browser-compatible JavaScript implementation with HTML demo interfaces
- **Language Bindings**: Each language implementation maintains API consistency while leveraging native language features

## Testing and Validation
- **Unit Testing Framework**: Comprehensive test suite using CMake's CTest framework
- **Cross-Platform Testing**: Automated testing across different operating systems and compiler configurations
- **Performance Testing**: Dedicated timing and performance measurement utilities
- **Expected Results Validation**: Extensive expected output files for regression testing

## Clustering and Analysis Tools
- **TLSH Clustering**: Python-based clustering algorithms including HAC-T (Hierarchical Agglomerative Clustering with TLSH) and DBSCAN implementations
- **Data Analysis**: Jupyter notebook-based analysis tools for malware dataset clustering and similarity analysis
- **Visualization**: Dendrogram generation and cluster visualization capabilities using matplotlib and scipy

## Build and Distribution
- **Cross-Platform Compilation**: Support for GCC, Clang, MSVC, and MinGW compilers
- **Package Management**: Integration with pip (Python), Maven/Gradle (Java), and npm (JavaScript) ecosystems
- **Documentation System**: HTML-based documentation with CSS styling and multi-page navigation

# External Dependencies

## Build Dependencies
- **CMake**: Version 3.x for cross-platform build configuration and project generation
- **C++ Compiler**: Modern C++ compiler with C++11 support (GCC, Clang, or MSVC)
- **Platform Tools**: Platform-specific development tools and libraries for Windows, Linux, and macOS

## Python Ecosystem
- **NumPy/SciPy**: Scientific computing libraries for clustering algorithms and mathematical operations
- **scikit-learn**: Machine learning library for DBSCAN clustering implementation
- **matplotlib**: Plotting library for dendrogram and cluster visualization
- **pandas**: Data manipulation library for dataset processing and analysis
- **Jupyter**: Interactive notebook environment for data analysis and visualization

## Java Dependencies
- **Gradle**: Build automation and dependency management
- **JUnit**: Testing framework for Java unit tests
- **Maven Central**: Distribution platform for Java artifacts

## Analysis and Security Tools
- **pefile**: Python library for PE (Portable Executable) file analysis and digital signature extraction
- **M2Crypto/pyOpenSSL**: Cryptographic libraries for certificate validation and digital signature processing
- **requests**: HTTP library for external API integrations and data fetching

## Documentation and Web
- **Static HTML/CSS**: Self-contained documentation system with responsive design
- **JavaScript**: Client-side TLSH implementation for web browser compatibility