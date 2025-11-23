#!/usr/bin/env python3
"""
Test script for jc_sdhash functionality
"""
import jc_sdhash as sd
import os
import time


def main():
    print("=== SDhash Python Wrapper Test ===")

    # Test file paths - MODIFIQUE AQUI PARA SEUS ARQUIVOS
    test_file = "pdf/doc10.pdf"  # ← Arquivo ORIGINAL
    sample_file = "pdf_50%/doc10_modified_50.0percent_contiguous.pdf"  # ← Arquivo ALTERADO
    hash_file1 = "test1.sdbf"
    hash_file2 = "test2.sdbf"

    # Test 1: Generate hash for existing test file
    print(f"\n1. Testing hash generation for '{test_file}'...")
    try:
        if os.path.exists(test_file):
            file_size = round(os.path.getsize(test_file) / (1024 * 1024), 2)
            print(f"   File size: {file_size} MB")

            start_time = time.time()
            result = sd.generate(test_file)
            end_time = time.time()
            execution_time = end_time - start_time

            print("✓ Hash generated successfully:")
            print(f"   ⏱️  Execution time: {execution_time:.3f} seconds")
            print(f"   📄 Hash preview: {result[:100]}..." if len(result) >
                  100 else f"   📄 Hash: {result}")
        else:
            print(f"✗ Test file '{test_file}' not found")
    except Exception as e:
        print(f"✗ Error generating hash: {e}")

    # Test 2: Generate hash and save to file
    print(f"\n2. Testing hash generation with output file...")
    try:
        if os.path.exists(sample_file):
            file_size = round(os.path.getsize(sample_file) / (1024 * 1024), 2)
            print(f"   File size: {file_size} MB")

            # Note: SDHash binary automatically appends .sdbf extension
            output_base = "doc1"

            start_time = time.time()
            sd.generate(sample_file, output_filepath=output_base)
            end_time = time.time()
            execution_time = end_time - start_time

            # Check for the actual created file (with .sdbf extension)
            expected_files = [
                f for f in os.listdir('.')
                if f.startswith(output_base) and f.endswith('.sdbf')
            ]
            if expected_files:
                actual_file = expected_files[0]
                print(f"✓ Hash saved to '{actual_file}' successfully")
                print(f"   ⏱️  Execution time: {execution_time:.3f} seconds")
                with open(actual_file, 'r') as f:
                    content = f.read()
                    print(f"   📄 File content preview: {content[:100]}...")
            else:
                print(
                    f"✗ Output file starting with '{output_base}' not created")
        else:
            print(f"✗ Sample file '{sample_file}' not found")
    except Exception as e:
        print(f"✗ Error generating hash with output: {e}")

    # Test 3: Generate hashes for both files and compare
    print(f"\n3. Testing hash generation and comparison...")
    overall_start_time = time.time()
    try:
        if os.path.exists(test_file) and os.path.exists(sample_file):
            file1_size = round(os.path.getsize(test_file) / (1024 * 1024), 2)
            file2_size = round(os.path.getsize(sample_file) / (1024 * 1024), 2)
            print(f"   File 1 size: {file1_size} MB")
            print(f"   File 2 size: {file2_size} MB")

            # Generate hashes for both files
            print(f"   Generating hash for '{test_file}'...")
            hash1_start = time.time()
            sd.generate(test_file, output_filepath="test1")
            hash1_time = time.time() - hash1_start

            print(f"   Generating hash for '{sample_file}'...")
            hash2_start = time.time()
            sd.generate(sample_file, output_filepath="test2")
            hash2_time = time.time() - hash2_start

            # Find the generated files
            hash1_files = [
                f for f in os.listdir('.')
                if f.startswith('test1') and f.endswith('.sdbf')
            ]
            hash2_files = [
                f for f in os.listdir('.')
                if f.startswith('test2') and f.endswith('.sdbf')
            ]

            if hash1_files and hash2_files:
                hash1_file = hash1_files[0]
                hash2_file = hash2_files[0]
                print(f"   Comparing '{hash1_file}' with '{hash2_file}'...")

                compare_start = time.time()
                result = sd.compare(hash1_file, hash2_file)
                compare_time = time.time() - compare_start
                overall_time = time.time() - overall_start_time

                print("✓ Comparison completed!")
                print(f"   ⏱️  Hash 1 time: {hash1_time:.3f} seconds")
                print(f"   ⏱️  Hash 2 time: {hash2_time:.3f} seconds")
                print(f"   ⏱️  Compare time: {compare_time:.3f} seconds")
                print(f"   ⏱️  Total time: {overall_time:.3f} seconds")

                if result.strip():
                    # Extract similarity percentage
                    parts = result.strip().split('|')
                    if len(parts) >= 3:
                        similarity = parts[-1]
                        print(f"   🎯 Similarity: {similarity}%")
                    else:
                        print(f"   🎯 Similarity result: {result.strip()}")
                else:
                    print(
                        "   📊 Similarity: 0% (arquivos são diferentes ou não têm similaridade detectável)"
                    )
            else:
                print("✗ Hash files not created properly")
        else:
            print(f"✗ Test files '{test_file}' or '{sample_file}' not found")
    except Exception as e:
        print(f"✗ Error in comparison test: {e}")

    # Test 4: Validate SDBF file
    print(f"\n4. Testing SDBF validation...")
    try:
        sdbf_files = [f for f in os.listdir('.') if f.endswith('.sdbf')]
        if sdbf_files:
            validation_start = time.time()
            result = sd.validate(sdbf_files[0])
            validation_time = time.time() - validation_start

            print(f"✓ Validation result for '{sdbf_files[0]}':")
            print(f"   ⏱️  Validation time: {validation_time:.3f} seconds")
            print(f"   📄 Result: {result}")
        else:
            print("✗ No SDBF files found for validation")
    except Exception as e:
        print(f"✗ Error validating file: {e}")

    print(f"\n=== Test Complete ===")


if __name__ == "__main__":
    main()
