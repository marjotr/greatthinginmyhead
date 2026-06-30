from google import genai

client = genai.Client(api_key="AQ.Ab8RN6IjFWWJJKg9nsuMjNfa4-fEcTKqdJLPosu4eSvPvSzPRA")

# LÓGICA DE LEITURA DE DADOS: O Python abre e lê o arquivo local
with open("dados_rio.txt", "r", encoding="utf-8") as arquivo:
    dados_locais = arquivo.read()

# O CONTEXTO AGORA RECEBE OS DADOS REAIS DA CIDADE
contexto_ambiental = (
    "Você é um cientista de dados especialista em sustentabilidade no Rio de Janeiro.\n"
    "Sua missão é responder à pergunta do usuário baseando-se estritamente nos dados fornecidos abaixo.\n"
    "Se a informação não estiver nos dados fornecidos, diga educadamente que não possui esse dado local.\n\n"
    f"=== DADOS LOCAIS DO RIO DE JANEIRO ===\n{dados_locais}"
)

# O usuário faz uma pergunta específica sobre o arquivo
pergunta_usuario = input("Digite sua dúvida sobre sustentabilidade: ")

resposta = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=f"{contexto_ambiental}\n\nPergunta: {pergunta_usuario}"
)

print(resposta.text)