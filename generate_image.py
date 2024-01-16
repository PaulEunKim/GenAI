import requests

def handle_response(message) -> str:
    p_message = message.lower()

    url = 'https://stablediffusionapi.com/api/v3/text2img'
    body = {
        "key": "D9Li9alxyLdqGghZVP00St51NFcm3nXjnGsYKUXdXMZacJvH32854iVDwVSW",
        "prompt": p_message,
        "negative_prompt": None,
        "width": "512",
        "height": "512",
        "samples": "1",
        "num_inference_steps": "20",
        "safety_checker": "no",
        "enhance_prompt": "yes",
        "seed": None,
        "guidance_scale": 7.5,
        "multi_lingual": "no",
        "panorama": "no",
        "self_attention": "no",
        "upscale": "no",
        "embeddings_model": "embeddings_model_id",
        "webhook": None,
        "track_id": None
    }

    print('hello')
    # sending get request and saving the response as response object
    r = requests.post(url=url, data=body, timeout=60)

    # extracting data in json format
    data = r.json()
    print(data)

    return data['output'][0]

