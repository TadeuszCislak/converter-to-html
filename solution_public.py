

import requests

# Ustawienia API
url = "https://api.openai.com/v1/chat/completions"
api_key = "XXXXX" # Tu wstaw klucz do API OpenAI 

# URL do pliku txt z artykułem
article_url = "https://cdn.oxido.pl/hr/Zadanie%20dla%20JJunior%20AI%20Developera%20-%20tresc%20artykulu.txt"

# Pobranie treści artykułu z podanego URL-a
response = requests.get(article_url)
if response.status_code == 200:
    article_content = response.text
else:
    print(f"Błąd przy pobieraniu artykułu: {response.status_code}")
    exit()
    
# Prompty do ilustracji w artykule
prompt1 = "An illustration representing the ethical and social challenges of artificial intelligence. Show a stylized digital brain, half made of circuits and code, and the other half symbolizing human values and ethics with icons like a scale for justice, a lock for privacy, and diverse human silhouettes. Around the brain, incorporate elements like data streams, symbols of transparency (such as an eye or open book), and soft gears to represent AI development processes. Use a modern and neutral color palette, with a calm and balanced composition that evokes both caution and hope for the future of AI."
prompt2 = "An illustration symbolizing automation and the future of the job market. Show a stylized factory or workspace where robotic arms and machines are working alongside human figures, representing collaboration between AI and people. Include elements like gears, code, and digital screens to suggest technological advancements, and show some figures learning or adapting, symbolizing education and skill-building. The scene should feel balanced, not overly futuristic, and use calm, neutral colors with hints of blue and gray to evoke a professional and thoughtful atmosphere on the future of work."
# Wcześniejsze testy wykazały dwa miejsca na ilustracje, dlatego prompty są dwa.

#Podpisy dla ilustracji
podpis1 = "AI może stanowić cenne wsparcie dla ludzkości, jednak jego rozwój musi przebiegać odpowiedzialnie"
podpis2 = "Wykorzystanie AI w pracy powinno iść w parze z powstaniem nowych możliwości pracy dla ludzi"

# Nagłówki zapytania
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# Prompt dla modelu do wygenerowania HTML
prompt = f"""
Przekształć poniższy artykuł na sekcję 'body' kodu HTML. Użyj odpowiednich znaczników HTML5 dla nagłówków (w tym śródtytułów), akapitów, figur i list, ale pomiń znaczniki <html></html>, <body></body> oraz oznaczenie "html" na początku. Zidentyfikuj miejsca w artykule, które byłyby najodpowiedniejsze dla umieszczenia w nich grafik, i oznacz je w kodzie za pomocą znaczników <figure></figure> i <img src="image_placeholder.jpg" />. Nadaj tym znacznikom atrybuty alt oraz umieść po nich podpisy do ilustracji zgodnie z poniższymi wytycznymi.

Artykuł:
{article_content}

Wartość atrybutu alt dla pierwszego znacznika:
{prompt1}

Podpis dla ilustracji z pierwszego znacznika:
{podpis1}

Wartość atrybutu alt dla drugiego znacznika:
{prompt2}

Podpis dla ilustracji z drugiego znacznika:
{podpis2}
"""

# Dane zapytania
data = {
    "model": "gpt-3.5-turbo",
    "messages": [
        {"role": "system", "content": "Jesteś asystentem generującym kod HTML."},
        {"role": "user", "content": prompt}
    ],
    "max_tokens": 4096
}

# Wysłanie żądania POST do API
response = requests.post(url, headers=headers, json=data)

# Sprawdzenie odpowiedzi
if response.status_code == 200:
    response_data = response.json()
    html_output = response_data["choices"][0]["message"]["content"]
     # Zapis do pliku HTML
    output_filename = "artykul.html"  # nazwa pliku wynikowego
    with open(output_filename, "w", encoding="utf-8") as file:
        file.write(html_output)
    
else:
    print(f"Błąd: {response.status_code}")
    print(response.text)
