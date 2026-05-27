
import argparse
import sys

def main():
    parser = argparse.ArgumentParser(
        prog="mkpixel",
        description="Generate procedural textures directly from your terminal."
    )
    parser.add_argument("prompt", type=str, help="Text description of the texture")
    parser.add_argument("-f", "--format", choices=["png", "jpg", "svg"], default="png", help="Output format")
    parser.add_argument("-s", "--size", type=int, default=512, help="Output resolution (default: 512x512)")
    parser.add_argument("-o", "--output", type=str, default=None, help="Custom output filename")

    args = parser.parse_args()

    print(f"🎨 Prompt: {args.prompt}")
    print(f"📐 Size: {args.size}x{args.size}")
    print(f"📦 Format: {args.format}")
    print("⚙️  Generating... (Core engine will be added in next step)")
    sys.exit(0)

if __name__ == "__main__":
    main()
