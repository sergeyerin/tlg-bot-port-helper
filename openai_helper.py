"""OpenAI helper functions for Portuguese language processing."""

import re
from openai import OpenAI
from config import OPENAI_API_KEY, OPENAI_MODEL, logger

# Initialize OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)

def is_single_verb(text: str) -> bool:
    """
    Determine if the input text is likely a single Portuguese verb.
    Returns True if it's a single word that could be a verb.
    """
    # Remove extra whitespace and convert to lowercase
    text = text.strip().lower()
    
    # Check if it's a single word (no spaces, punctuation, etc.)
    if not re.match(r'^[a-záàâãéêíóôõúçñü]+$', text):
        return False
    
    # Additional heuristics: single words with 3+ characters are likely verbs
    return len(text) >= 3

async def conjugate_verb(verb: str) -> str:
    """
    Get all conjugations of a Portuguese verb using OpenAI.
    """
    try:
        prompt = f"""
You are a Portuguese language expert. Given the Portuguese verb "{verb}" (in any form), provide ALL possible conjugations organized by tense and person.

Please format the response exactly like this example:

**VERBO: {verb.upper()}**

**INFINITIVO:**
• Infinitivo: [infinitive form]

**PRESENTE DO INDICATIVO:**
• Eu [conjugation]
• Tu [conjugation]
• Ele/Ela [conjugation]
• Nós [conjugation]
• Vós [conjugation]
• Eles/Elas [conjugation]

**PRETÉRITO PERFEITO:**
• Eu [conjugation]
• Tu [conjugation]
• Ele/Ela [conjugation]
• Nós [conjugation]
• Vós [conjugation]
• Eles/Elas [conjugation]

**PRETÉRITO IMPERFEITO:**
• Eu [conjugation]
• Tu [conjugation]
• Ele/Ela [conjugation]
• Nós [conjugation]
• Vós [conjugation]
• Eles/Elas [conjugation]

**FUTURO DO PRESENTE:**
• Eu [conjugation]
• Tu [conjugation]
• Ele/Ela [conjugation]
• Nós [conjugation]
• Vós [conjugation]
• Eles/Elas [conjugation]

**CONDICIONAL:**
• Eu [conjugation]
• Tu [conjugation]
• Ele/Ela [conjugation]
• Nós [conjugation]
• Vós [conjugation]
• Eles/Elas [conjugation]

**PRESENTE DO SUBJUNTIVO:**
• Que eu [conjugation]
• Que tu [conjugation]
• Que ele/ela [conjugation]
• Que nós [conjugation]
• Que vós [conjugation]
• Que eles/elas [conjugation]

**IMPERATIVO:**
• Tu [conjugation]
• Ele/Ela [conjugation]
• Nós [conjugation]
• Vós [conjugation]
• Eles/Elas [conjugation]

If the word is not a valid Portuguese verb, respond with: "❌ '{verb}' não parece ser um verbo português válido."
"""

        response = client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=[
                {"role": "system", "content": "You are a Portuguese language expert specializing in verb conjugations."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1500,
            temperature=0.1
        )
        
        return response.choices[0].message.content.strip()
    
    except Exception as e:
        logger.error(f"Error conjugating verb '{verb}': {e}")
        return f"❌ Erro ao conjugar o verbo '{verb}'. Tente novamente mais tarde."

async def correct_phrase(phrase: str) -> str:
    """
    Correct Portuguese phrase and explain errors using OpenAI.
    """
    try:
        prompt = f"""
You are a Portuguese language teacher. Analyze the following Portuguese phrase and:

1. If there are grammatical errors, provide the corrected version
2. Explain what was wrong and why
3. If the phrase is already correct, just say it's correct

Phrase to analyze: "{phrase}"

Format your response like this:

**FRASE ORIGINAL:** {phrase}

**FRASE CORRIGIDA:** [corrected phrase or "A frase está correta!"]

**EXPLICAÇÃO:**
[Detailed explanation in Portuguese about what was wrong and why, or confirmation that it's correct. Include grammar rules if applicable.]

Be encouraging and educational in your explanations.
"""

        response = client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=[
                {"role": "system", "content": "You are a helpful Portuguese language teacher who corrects grammar mistakes and explains them clearly in Portuguese."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1000,
            temperature=0.1
        )
        
        return response.choices[0].message.content.strip()
    
    except Exception as e:
        logger.error(f"Error correcting phrase '{phrase}': {e}")
        return f"❌ Erro ao corrigir a frase. Tente novamente mais tarde."

async def process_text(text: str) -> str:
    """
    Process user input and determine whether to conjugate a verb or correct a phrase.
    """
    text = text.strip()
    
    if not text:
        return "❌ Por favor, envie um texto para processar."
    
    # Check if it's likely a single verb
    if is_single_verb(text):
        logger.info(f"Processing '{text}' as a verb for conjugation")
        return await conjugate_verb(text)
    else:
        logger.info(f"Processing '{text}' as a phrase for correction")
        return await correct_phrase(text)