"""Entry for make.fun: Everyday Things, Two Lines, Longer Run."""
import os

# Entry text: 257 characters (limit 400), 2 line(s), no trailing newline.
ENTRY = 'A toaster is like a tiny sunbed for bread: it lies down, soaks up heat, and pops up brown when it has had enough.\nThe comparison works because heat browns both skin and bread, but it leaves out that bread never chooses when it is done — the toaster decides.'

def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
