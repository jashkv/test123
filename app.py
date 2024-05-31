import requests

def fetch_top_models():
    url = "https://huggingface.co/api/models"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  
        models = response.json()

        if isinstance(models, list):
            sorted_models = sorted(models, key=lambda x: x.get('downloads', 0), reverse=True)
            top_10_models = sorted_models[:10]
            
            report = "Top 10 Downloaded Models on Hugging Face:\n"
            for idx, model in enumerate(top_10_models, start=1):
                report += f"{idx}. {model.get('modelId', 'Unknown')} - Downloads: {model.get('downloads', 'Unknown')}\n"
            
            with open("/report/top_10_models.txt", "w") as file:
                file.write(report)
        else:
            print("Unexpected response format")
    
    except requests.RequestException as e:
        print(f"An error occurred while fetching data: {e}")

if __name__ == "__main__":
    fetch_top_models()
