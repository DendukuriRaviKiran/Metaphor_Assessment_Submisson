# Shopping Assistant Using Metaphor API

## YouTube Demo Link
[Watch the Demo](https://www.youtube.com/watch?v=VIFC3RWQg0k)
## 1. Brief Explanation of Project

Are you a fashion enthusiast who loves finding celebrity-inspired outfits or recreating manga character looks? The "Shopping Assistant Using Metaphor API" is here to make your shopping experience even more exciting and customizable.

- **Problem**: Google Lens lacks the customization options for filtering shopping results based on marketplace, price, and delivery date.

- **Solution**: We've developed a versatile shopping assistant using the Metaphor API. It empowers you to:
  - Upload images of your fashion inspirations.
  - Generate or edit images for your ideal fashion items.
  - Automatically caption images.
  - Discover shopping links related to your fashion choices.
  - Customize your search by preferred marketplace domains.

Plus, we've integrated a stable diffusion model for image generation, making your shopping journey immersive and enjoyable.

## 2. How it's Built

The Shopping Assistant is built with four main phases:

1. **Image Upload/Generation**: Users can upload or generate/edit images to use as fashion inspiration.

2. **Image Captioning**: An image-to-text captioning algorithm (Blip) processes the images and generates descriptive captions.

3. **Finding Similar Links using Metaphor API**: The generated captions are used to query the Metaphor API to find shopping links related to the described clothing or items.

4. **Filtering Links using Metaphor API**: Users can customize their search by specifying their preferred marketplace domains, and a cosine similarity algorithm is used to find the best matching shopping links.

## How to Use

To run the shopping assistant locally, follow these steps:

1. Clone this repository to your local machine.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Run the Streamlit app using `streamlit run app.py`.

## Enhancing the Shopping Experience

To further enhance the shopping experience:

- Implement query correction and synonyms to address user query inaccuracies.
- Include additional metadata like price, product image, ratings, and availability for better product insights.



## License

This project is licensed under the [MIT License](LICENSE).
