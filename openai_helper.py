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
    Get all conjugations of a Portuguese verb using OpenAI with European Portuguese focus.
    """
    try:
        prompt = f"""
You are an expert in European Portuguese (português europeu) helping Russian speakers learn Portuguese. Given the Portuguese verb "{verb}" (in any form), provide ALL possible conjugations organized by tense and person using EUROPEAN PORTUGUESE standards and spelling.

IMPORTANT: Use European Portuguese conventions including:
- Closed vowels (ê, ô) where appropriate
- European Portuguese spelling and pronunciation patterns
- Formal register with "tu" and "vós" forms

Please format the response exactly like this example:

**ГЛАГОЛ: {verb.upper()}**

**ИНФИНИТИВ:**
• Infinitivo: [infinitive form]

**НАСТОЯЩЕЕ ВРЕМЯ (PRESENTE DO INDICATIVO):**
• Eu [conjugation]
• Tu [conjugation]
• Ele/Ela [conjugation]
• Nós [conjugation]
• Vós [conjugation]
• Eles/Elas [conjugation]

**ПРОСТОЕ ПРОШЕДШЕЕ (PRETÉRITO PERFEITO):**
• Eu [conjugation]
• Tu [conjugation]
• Ele/Ela [conjugation]
• Nós [conjugation]
• Vós [conjugation]
• Eles/Elas [conjugation]

**НЕЗАВЕРШЕННОЕ ПРОШЕДШЕЕ (PRETÉRITO IMPERFEITO):**
• Eu [conjugation]
• Tu [conjugation]
• Ele/Ela [conjugation]
• Nós [conjugation]
• Vós [conjugation]
• Eles/Elas [conjugation]

**ПРОСТОЕ БУДУЩЕЕ (FUTURO DO PRESENTE):**
• Eu [conjugation]
• Tu [conjugation]
• Ele/Ela [conjugation]
• Nós [conjugation]
• Vós [conjugation]
• Eles/Elas [conjugations]

**УСЛОВНОЕ НАКЛОНЕНИЕ (CONDICIONAL):**
• Eu [conjugation]
• Tu [conjugation]
• Ele/Ela [conjugation]
• Nós [conjugation]
• Vós [conjugation]
• Eles/Elas [conjugation]

**СОСЛАГАТЕЛЬНОЕ НАКЛОНЕНИЕ (PRESENTE DO SUBJUNTIVO):**
• Que eu [conjugation]
• Que tu [conjugation]
• Que ele/ela [conjugation]
• Que nós [conjugation]
• Que vós [conjugation]
• Que eles/elas [conjugation]

**ПОВЕЛИТЕЛЬНОЕ НАКЛОНЕНИЕ (IMPERATIVO):**
• Tu [conjugation]
• Ele/Ela [conjugation]
• Nós [conjugation]
• Vós [conjugation]
• Eles/Elas [conjugation]

If the word is not a valid Portuguese verb, respond with: "❌ '{verb}' не является действительным португальским глаголом."
"""

        response = client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=[
                {"role": "system", "content": "You are an expert in European Portuguese (português europeu) helping Russian speakers learn Portuguese. You specialize in verb conjugations using European Portuguese standards and provide explanations in Russian. Always double-check your conjugations for accuracy."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1500,
            temperature=0.1
        )
        
        return response.choices[0].message.content.strip()
    
    except Exception as e:
        logger.error(f"Error conjugating verb '{verb}': {e}")
        return f"❌ Ошибка при спряжении глагола '{verb}'. Попробуйте снова позже."

async def correct_phrase(phrase: str) -> str:
    """
    Correct Portuguese phrase with focus on prepositions using European Portuguese standards.
    """
    try:
        prompt = f"""
You are an expert European Portuguese (português europeu) teacher helping Russian speakers learn Portuguese. Analyze the following Portuguese phrase with SPECIAL ATTENTION to prepositions and their correct usage.

CRITICAL REQUIREMENTS:
1. Use EUROPEAN PORTUGUESE standards and spelling (not Brazilian Portuguese)
2. DOUBLE-CHECK all prepositions (de, em, por, para, a, com, sobre, entre, etc.) for accuracy
3. Pay extra attention to preposition contractions (do, da, no, na, pelo, pela, ao, à, etc.)
4. Verify verb-preposition combinations (phrasal verbs)
5. Check for correct usage of "a" vs "para" vs "de" vs "em"
6. Ensure proper agreement and placement of prepositions

Phrase to analyze: "{phrase}"

STEPS TO FOLLOW:
1. First, identify ALL prepositions in the phrase
2. Check each preposition for correctness in context
3. Verify preposition contractions are properly formed
4. Double-check verb-preposition combinations
5. Provide corrected version if needed

Format your response like this:

**ИСХОДНАЯ ФРАЗА:** {phrase}

**ИСПРАВЛЕННАЯ ФРАЗА:** [corrected phrase using European Portuguese OR "Фраза верна!"]

**АНАЛИЗ ПРЕДЛОГОВ:**
[List all prepositions found and verify their correctness]

**ОБЪЯСНЕНИЕ:**
[Detailed explanation IN RUSSIAN about:
- What preposition errors were found (if any)
- Why the corrections were made
- Rules for proper preposition usage
- European Portuguese vs Brazilian differences if relevant
- Grammar rules that apply]

**ПРАВИЛО:** [Key grammar rule to remember, if applicable]

Be thorough, encouraging and educational. Write all explanations in Russian language. Always double-check your corrections before providing the final answer.
"""

        response = client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=[
                {"role": "system", "content": "You are an expert European Portuguese teacher specializing in preposition corrections and grammar analysis. You help Russian-speaking students by providing detailed, accurate corrections with special focus on prepositions. Always double-check your corrections for accuracy and use European Portuguese standards. Provide thorough explanations in Russian."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1200,
            temperature=0.1
        )
        
        return response.choices[0].message.content.strip()
    
    except Exception as e:
        logger.error(f"Error correcting phrase '{phrase}': {e}")
        return f"❌ Ошибка при исправлении фразы. Попробуйте снова позже."

async def process_text(text: str) -> str:
    """
    Process user input and determine whether to conjugate a verb or correct a phrase.
    """
    text = text.strip()
    
    if not text:
        return "❌ Пожалуйста, отправьте текст для обработки."
    
    # Check if it's likely a single verb
    if is_single_verb(text):
        logger.info(f"Processing '{text}' as a verb for conjugation")
        return await conjugate_verb(text)
    else:
        logger.info(f"Processing '{text}' as a phrase for correction")
        return await correct_phrase(text)