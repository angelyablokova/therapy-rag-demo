# 1. Словарь ключевых слов и реакций
triggers = {
    "суицид": "‼️ Обнаружен риск: немедленно обратитесь за помощью.",
    "депрессия": "📉 Симптомы депрессии. Рекомендуется самонаблюдение и консультация.",
    "тревога": "⚠️ Отмечается тревожность — проверьте интенсивность и продолжительность."
}

# 2. Функция анализа, возвращающая список найденных рисков
def analyze_response(text):
    text_lower = text.lower()
    detected = []

    for keyword, message in triggers.items():
        if keyword in text_lower:
            detected.append((keyword, message))

    return detected

# 3. Получение текста от пользователя
user_input = input("Введите текст сессии или сообщения клиента:\n")
results = analyze_response(user_input)

# 4. Вывод результата
if results:
    print("🚩 Обнаружены ключевые слова:", ", ".join([word for word, _ in results]))
    print("📋 Рекомендации:")
    for _, message in results:
        print(" -", message)
else:
    print("✅ Текст не содержит признаков риска.")
