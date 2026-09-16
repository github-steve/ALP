from PIL import Image, ImageDraw, ImageFont
import os

WATERMARK_TEXT = "© Mandy Budan"
OPACITY = 0.4
SIZE_PCT = 2.5

def add_watermark(input_path, output_path):
    """Add visible watermark to image."""
    img = Image.open(input_path).convert("RGBA")
    w, h = img.size
    
    overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    
    font_size = int(h * SIZE_PCT / 100)
    font_size = max(font_size, 10)  # minimum size
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", font_size)
    except:
        font = ImageFont.load_default()
    
    bbox = draw.textbbox((0, 0), WATERMARK_TEXT, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    padding = max(int(h * 0.015), 5)
    
    x = w - tw - padding
    y = h - th - padding
    
    draw.text((x, y), WATERMARK_TEXT, font=font, fill=(255, 255, 255, int(255 * OPACITY)))
    
    result = Image.alpha_composite(img, overlay).convert("RGB")
    result.save(output_path, "JPEG", quality=90)

def main():
    base_dir = "/Users/hermesagent/workspace/alp_warm"
    painting_dir = os.path.join(base_dir, "images")
    study_dir = os.path.join(base_dir, "images", "studies2")
    
    tasks = []
    
    # Paintings: gallery + detail
    for f in sorted(os.listdir(painting_dir)):
        if f.endswith('.jpg') and not f.endswith('_sm.jpg'):
            path = os.path.join(painting_dir, f)
            tasks.append((path, "PAINTING"))
    
    # Studies: gallery (_sm) + detail
    for f in sorted(os.listdir(study_dir)):
        if f.endswith('.jpg'):
            path = os.path.join(study_dir, f)
            kind = "STUDY-GALLERY" if '_sm' in f else "STUDY-DETAIL"
            tasks.append((path, kind))
    
    print(f"Watermarking {len(tasks)} images...")
    print(f"Text: {WATERMARK_TEXT}, Opacity: {OPACITY*100}%, Size: {SIZE_PCT}%")
    print()
    
    success = 0
    failed = 0
    
    for i, (path, task_type) in enumerate(tasks):
        try:
            add_watermark(path, path)
            rel_path = os.path.relpath(path, base_dir)
            print(f"{i+1:3d}/{len(tasks)} [{task_type:14s}] ✅ {rel_path}")
            success += 1
        except Exception as e:
            rel_path = os.path.relpath(path, base_dir)
            print(f"{i+1:3d}/{len(tasks)} [{task_type:14s}] ❌ {rel_path} - {e}")
            failed += 1
    
    print()
    print(f"{'='*60}")
    print(f"Done: {success} success, {failed} failed out of {len(tasks)}")

if __name__ == "__main__":
    main()
