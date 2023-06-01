import os
import requests

# Получите токен вашего телеграм-бота
TELEGRAM_BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"


def send_message():
    chat_id = 808945403  # Замените на ваш chat_id
    total_tests = os.environ.get('TOTAL_TESTS', 'N/A')
    passed_tests = os.environ.get('PASSED_TESTS', 'N/A')
    failed_tests = os.environ.get('FAILED_TESTS', 'N/A')
    skipped_tests = os.environ.get('SKIPPED_TESTS', 'N/A')

    message = f"Результаты выполнения тестов:\n" \
              f"Всего тестов: {total_tests}\n" \
              f"Пройдено: {passed_tests}\n" \
              f"Провалено: {failed_tests}\n" \
              f"Пропущено: {skipped_tests}"

    payload = {
        "chat_id": chat_id,
        "text": message
    }

    response = requests.post(url, json=payload)
    if response.status_code == 200:
        print("Сообщение успешно отправлено")
    else:
        print("Ошибка при отправке сообщения:", response.status_code)


send_message()
