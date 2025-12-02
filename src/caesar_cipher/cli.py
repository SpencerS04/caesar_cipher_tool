import argparse
import random
from caesar_cipher import encrypt, decrypt

def main():
    parser = argparse.ArgumentParser(
        description="Caesar cipher command-line tool"
    )
    parser.add_argument(
        "mode",
        choices=["encrypt", "e", "d", "decrypt"],
        help="Whether to encrypt or decrypt the input file",
    )
    parser.add_argument(
        "infile",
        help="Path to the input text file",
    )
    parser.add_argument(
        "outfile",
        help="Path to the output text file",
    )
    parser.add_argument(
        "-s", "--shift",
        type=int,
        help="Shift value (1–25). If omitted, a random shift is used for encryption.",
    )
    
    args = parser.parse_args()
    
    # decide shift value
    if args.shift is None:
        if args.mode == "encrypt":
            shift = random.randint(1, 25)
            print(f"Using random shift: {shift}")
        else:
            raise SystemExit(
                "Error: you must provide --shift for decrypt mode (no random key)."
            )
    else:
        shift = args.shift
        if not (1 <= shift <= 25):
            raise SystemExit("Error: shift must be in the range 1–25.")
        
    # read input
    with open(args.infile, "rt") as f:
        file_content = f.read()
        
    # calculate
    if args.mode == "encrypt" or args.mode == "e":
        output_text = encrypt(file_content, shift)
    else:
        output_text = decrypt(file_content, shift)
        
    # write output
    with open(args.outfile, "wt") as f:
        f.write(output_text)
        
if __name__ == "__main__":
    main()