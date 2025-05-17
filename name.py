from google.cloud import vision

def detect_top_celebrity_name(image_path):
    client = vision.ImageAnnotatorClient()

    with open(image_path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)
    response = client.web_detection(image=image)

    web_detection = response.web_detection

    if web_detection.web_entities:
        top_entity = web_detection.web_entities[0]
        return top_entity.description
    else:
        return "Unknown person"

if __name__ == "__main__":
    # Replace this with the path to your image
    result = detect_top_celebrity_name("/Users/suryadeepsinhjadeja/Desktop/Screenshot 2025-05-17 at 11.04.32 PM.png")
    print(result)