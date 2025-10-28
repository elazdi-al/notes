#!/usr/bin/env python3
"""
Algorithm Image to LaTeX Converter

This script uses OpenAI's vision model to analyze algorithm images
and convert them into LaTeX algorithmic code blocks.
"""

import os
import base64
from pathlib import Path
from openai import OpenAI
import re

class AlgorithmImageConverter:
    def __init__(self, api_key=None):
        """Initialize the converter with OpenAI API key"""
        self.client = OpenAI(api_key=api_key or os.getenv('OPENAI_API_KEY'))
        self.images_dir = Path('images')
        self.codes_dir = Path('codes')
        
        # Create codes directory if it doesn't exist
        self.codes_dir.mkdir(exist_ok=True)
        
        # Supported image formats
        self.supported_formats = {'.png', '.jpg', '.jpeg', '.gif', '.webp'}
    
    def encode_image_to_base64(self, image_path):
        """Encode image to base64 string"""
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')
    
    def get_image_mime_type(self, image_path):
        """Get MIME type for image"""
        suffix = Path(image_path).suffix.lower()
        mime_types = {
            '.png': 'image/png',
            '.jpg': 'image/jpeg',
            '.jpeg': 'image/jpeg',
            '.gif': 'image/gif',
            '.webp': 'image/webp'
        }
        return mime_types.get(suffix, 'image/png')
    
    def analyze_algorithm_image(self, image_path):
        """Use OpenAI Vision to analyze algorithm image and convert to LaTeX"""
        
        base64_image = self.encode_image_to_base64(image_path)
        mime_type = self.get_image_mime_type(image_path)
        
        prompt = """
        You are an expert in algorithms and LaTeX formatting. Analyze this image that contains algorithm pseudocode.

        Your task:
        1. Extract the exact algorithm(s) shown in the image
        2. Convert to LaTeX algorithmic format
        3. Do NOT include line numbers even if they appear in the image
        4. Output should start with \\begin{algorithmic} and end with \\end{algorithmic}
        5. If there are multiple algorithms in the image, create separate \\begin{algorithmic}...\\end{algorithmic} blocks for each
        6. Use proper LaTeX algorithmic commands like \\State, \\If, \\EndIf, \\For, \\EndFor, \\While, \\EndWhile, \\Function, \\EndFunction, etc.
        7. Preserve the exact algorithm logic, variable names, and structure
        8. Do not add any explanatory text - only output the LaTeX code

        Example format:
        \\begin{algorithmic}
        \\Function{FunctionName}{parameters}
        \\State statement
        \\If{condition}
        \\State statement
        \\EndIf
        \\Return{value}
        \\EndFunction
        \\end{algorithmic}

        Output ONLY the LaTeX algorithmic code blocks, nothing else.
        """
        
        try:
            response = self.client.chat.completions.create(
                model="o4-mini",  # Using GPT-4 with vision
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {"type": "text", "text": prompt},
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": f"data:{mime_type};base64,{base64_image}",
                                    "detail": "high"
                                }
                            }
                        ]
                    }
                ],
            )
            
            return response.choices[0].message.content.strip()
            
        except Exception as e:
            print(f"Error analyzing image {image_path}: {str(e)}")
            return None
    
    def clean_latex_output(self, latex_code):
        """Clean and validate LaTeX output"""
        if not latex_code:
            return None
            
        # Remove any markdown code blocks if present
        latex_code = re.sub(r'```latex\n?', '', latex_code)
        latex_code = re.sub(r'```\n?', '', latex_code)
        
        # Ensure proper formatting
        latex_code = latex_code.strip()
        
        return latex_code
    
    def save_latex_code(self, latex_code, output_path):
        """Save LaTeX code to file"""
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(latex_code)
            print(f"✓ Saved: {output_path}")
            return True
        except Exception as e:
            print(f"✗ Error saving {output_path}: {str(e)}")
            return False
    
    def process_single_image(self, image_path):
        """Process a single image file"""
        print(f"Processing: {image_path.name}")
        
        # Analyze image with OpenAI Vision
        latex_code = self.analyze_algorithm_image(image_path)
        
        if not latex_code:
            print(f"✗ Failed to analyze: {image_path.name}")
            return False
        
        # Clean the output
        cleaned_code = self.clean_latex_output(latex_code)
        
        if not cleaned_code:
            print(f"✗ No valid LaTeX code extracted from: {image_path.name}")
            return False
        
        # Generate output filename
        base_name = image_path.stem  # filename without extension
        output_path = self.codes_dir / f"{base_name}.tex"
        
        # Save the LaTeX code
        return self.save_latex_code(cleaned_code, output_path)
    
    def process_all_images(self):
        """Process all images in the images directory"""
        if not self.images_dir.exists():
            print(f"Error: Images directory '{self.images_dir}' not found!")
            return
        
        # Get all image files
        image_files = []
        for suffix in self.supported_formats:
            image_files.extend(self.images_dir.glob(f"*{suffix}"))
        
        if not image_files:
            print("No supported image files found in images directory!")
            return
        
        print(f"Found {len(image_files)} image files to process...")
        print("=" * 50)
        
        successful = 0
        failed = 0
        
        for image_path in sorted(image_files):
            # Skip .DS_Store and other system files
            if image_path.name.startswith('.'):
                continue
                
            if self.process_single_image(image_path):
                successful += 1
            else:
                failed += 1
        
        print("=" * 50)
        print(f"Processing complete!")
        print(f"✓ Successful: {successful}")
        print(f"✗ Failed: {failed}")
        print(f"Output directory: {self.codes_dir.absolute()}")

def main():
    """Main function"""
    print("Algorithm Image to LaTeX Converter")
    print("=" * 40)
    
    # Check for OpenAI API key
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        print("Error: Please set your OpenAI API key as environment variable:")
        print("export OPENAI_API_KEY='your-api-key-here'")
        return
    
    # Initialize converter and process images
    converter = AlgorithmImageConverter(api_key)
    converter.process_all_images()

if __name__ == "__main__":
    main()
