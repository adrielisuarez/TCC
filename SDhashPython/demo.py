#!/usr/bin/env python3
"""
Interactive demo for jc_sdhash - SDHash Python Wrapper
This demonstrates all the functionality of the SDHash Python wrapper.
"""
import jc_sdhash as sd
import os
import sys

def print_banner():
    print("=" * 60)
    print("  SDHash Python Wrapper - Interactive Demo")
    print("  A Python wrapper for the SDHash binary")
    print("=" * 60)

def print_section(title):
    print(f"\n{'='*20} {title} {'='*20}")

def demo_hash_generation():
    print_section("Hash Generation Demo")
    
    # Create a sample file
    sample_content = "Hello, this is a sample file for SDHash demonstration.\nSDHash is a similarity-preserving hash function."
    with open("demo_sample.txt", "w") as f:
        f.write(sample_content)
    
    print("1. Creating sample file 'demo_sample.txt'...")
    print(f"   Content: {sample_content[:50]}...")
    
    print("\n2. Generating SDBF hash for the sample file...")
    try:
        hash_result = sd.generate("demo_sample.txt")
        print("   ✓ Hash generation successful!")
        print(f"   Hash preview: {hash_result[:80]}...")
        return True
    except Exception as e:
        print(f"   ✗ Error: {e}")
        return False

def demo_hash_save():
    print_section("Save Hash to File Demo")
    
    print("1. Generating hash and saving to 'demo_output.sdbf'...")
    try:
        # Note: sdhash binary automatically appends .sdbf extension
        sd.generate("demo_sample.txt", output_filepath="demo_output")
        
        # Check if file was created (with .sdbf extension)
        output_files = [f for f in os.listdir('.') if f.startswith('demo_output') and f.endswith('.sdbf')]
        if output_files:
            actual_file = output_files[0]
            print(f"   ✓ Hash saved to '{actual_file}'")
            with open(actual_file, 'r') as f:
                content = f.read()
                print(f"   File content preview: {content[:60]}...")
            return actual_file
        else:
            print("   ✗ Output file not found")
            return None
    except Exception as e:
        print(f"   ✗ Error: {e}")
        return None

def demo_hash_comparison():
    print_section("Hash Comparison Demo")
    
    # Create a second sample file with slight differences
    sample_content2 = "Hello, this is a sample file for SDHash demonstration.\nSDHash is a similarity-preserving hash function with great performance."
    with open("demo_sample2.txt", "w") as f:
        f.write(sample_content2)
    
    print("1. Creating second sample file with slight differences...")
    print("2. Generating hashes for both files...")
    
    try:
        # Generate hashes for both files
        sd.generate("demo_sample.txt", output_filepath="demo_hash1")
        sd.generate("demo_sample2.txt", output_filepath="demo_hash2")
        
        # Find the actual filenames (with .sdbf extension)
        hash1_files = [f for f in os.listdir('.') if f.startswith('demo_hash1') and f.endswith('.sdbf')]
        hash2_files = [f for f in os.listdir('.') if f.startswith('demo_hash2') and f.endswith('.sdbf')]
        
        if hash1_files and hash2_files:
            hash1_file = hash1_files[0]
            hash2_file = hash2_files[0]
            
            print(f"3. Comparing '{hash1_file}' and '{hash2_file}'...")
            result = sd.compare(hash1_file, hash2_file)
            print("   ✓ Comparison completed!")
            if result.strip():
                print(f"   Similarity result: {result.strip()}")
            else:
                print("   Similarity: 0 (files are different)")
        else:
            print("   ✗ Hash files not found")
    except Exception as e:
        print(f"   ✗ Error: {e}")

def demo_hash_validation():
    print_section("Hash Validation Demo")
    
    # Use existing SDBF files for validation
    sdbf_files = [f for f in os.listdir('.') if f.endswith('.sdbf')]
    
    if sdbf_files:
        test_file = sdbf_files[0]
        print(f"1. Validating SDBF file '{test_file}'...")
        try:
            result = sd.validate(test_file)
            print("   ✓ Validation completed!")
            print(f"   Result: {result.strip()}")
        except Exception as e:
            print(f"   ✗ Error: {e}")
    else:
        print("   ✗ No SDBF files found for validation")

def show_available_files():
    print_section("Available Files")
    
    files = os.listdir('.')
    txt_files = [f for f in files if f.endswith('.txt')]
    sdbf_files = [f for f in files if f.endswith('.sdbf')]
    
    print(f"Text files ({len(txt_files)}):")
    for f in txt_files:
        size = os.path.getsize(f)
        print(f"  - {f} ({size} bytes)")
    
    print(f"\nSDBF hash files ({len(sdbf_files)}):")
    for f in sdbf_files:
        size = os.path.getsize(f)
        print(f"  - {f} ({size} bytes)")

def cleanup_demo_files():
    """Clean up demo files"""
    demo_files = [
        'demo_sample.txt', 'demo_sample2.txt',
        'demo_output.sdbf', 'demo_hash1.sdbf', 'demo_hash2.sdbf'
    ]
    
    removed = []
    for file in demo_files:
        if os.path.exists(file):
            os.remove(file)
            removed.append(file)
    
    if removed:
        print(f"\nCleaned up demo files: {', '.join(removed)}")

def main():
    try:
        print_banner()
        
        # Check if SDHash is working
        print("\nChecking SDHash installation...")
        try:
            # Test with existing file
            if os.path.exists("test.txt"):
                result = sd.generate("test.txt")
                print("✓ SDHash is working properly!")
            else:
                print("✓ SDHash Python wrapper loaded successfully!")
        except Exception as e:
            print(f"✗ SDHash check failed: {e}")
            return
        
        # Run all demos
        demo_hash_generation()
        demo_hash_save()
        demo_hash_comparison()
        demo_hash_validation()
        show_available_files()
        
        print("\n" + "="*60)
        print("  Demo completed successfully!")
        print("  You can now use jc_sdhash in your Python projects.")
        print("="*60)
        
        # Ask if user wants to clean up
        print("\nDemo files created. They will remain for your reference.")
        
    except KeyboardInterrupt:
        print("\n\nDemo interrupted by user.")
    except Exception as e:
        print(f"\nUnexpected error: {e}")
    finally:
        print("\nDemo finished.")

if __name__ == "__main__":
    main()