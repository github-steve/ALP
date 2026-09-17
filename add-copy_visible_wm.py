from PIL import Image, ImageDraw, ImageFont, ImageEnhance
import os

def add_visible_watermark(input_path, output_path, text="© Mandy Budan", position="se", opacity=0.5, size_pct=3):
    """Add visible watermark to image.
    
    position: 'nw', 'ne', 'sw', 'se' (corners)
    opacity: 0.0 to 1.0
    size_pct: font size as percentage of image height
    """
    img = Image.open(input_path).convert("RGBA")
    w, h = img.size
    
    # Create transparent overlay
    overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    
    # Font size
    font_size = int(h * size_pct / 100)
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", font_size)
    except:
        font = ImageFont.load_default()
    
    # Text position
    bbox = draw.textbbox((0, 0), text, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    padding = int(h * 0.015)  # 1.5% padding
    
    positions = {
        "nw": (padding, padding),
        "ne": (w - tw - padding, padding),
        "sw": (padding, h - th - padding),
        "se": (w - tw - padding, h - th - padding),
    }
    x, y = positions.get(position, positions["se"])
    
    # Draw text on overlay
    draw.text((x, y), text, font=font, fill=(255, 255, 255, int(255 * opacity)))
    
    # Composite
    result = Image.alpha_composite(img, overlay)
    
    # Convert back to RGB for JPEG
    result = result.convert("RGB")
    
    # Save
    result.save(output_path, "JPEG", quality=90)
    print(f"Saved: {output_path}")

# Test on one painting and one study
painting = "/Users/hermesagent/workspace/alp_warm/images/2009-in-a-pine-forest_detail.jpg"
study = "/Users/hermesagent/workspace/alp_warm/images/studies2/2025-223_detail.jpg"

add_visible_watermark(painting, "/tmp/wm_painting_se.jpg", "© Mandy Budan", "se", 0.4, 2.5)
add_visible_watermark(study, "/tmp/wm_study_se.jpg", "© Mandy Budan", "se", 0.4, 2.5)

print("Done")
