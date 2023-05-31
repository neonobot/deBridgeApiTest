import os

from telegram import Bot

# Получите токен вашего телеграм-бота
TELEGRAM_BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')


def send_message():
    # Получите токен вашего телеграм-бота
    telegram_bot_token = os.environ.get('TELEGRAM_BOT_TOKEN')

    # Замените <chat_id> на ваш идентификатор чата или группы, куда нужно отправить сообщение
    chat_id = '808945403'

    # Получите информацию о результатах выполнения тестов из контекста выполнения GitHub Actions
    total_tests = os.environ.get('TOTAL_TESTS', 'N/A')
    passed_tests = os.environ.get('PASSED_TESTS', 'N/A')
    failed_tests = os.environ.get('FAILED_TESTS', 'N/A')
    skipped_tests = os.environ.get('SKIPPED_TESTS', 'N/A')

    # Формируем текст сообщения
    message = f"Результаты выполнения тестов:\n" \
              f"Всего тестов: {total_tests}\n" \
              f"Пройдено: {passed_tests}\n" \
              f"Провалено: {failed_tests}\n" \
              f"Пропущено: {skipped_tests}"

    # Создаем экземпляр бота
    bot = Bot(token=telegram_bot_token)

    # Отправляем сообщение
    bot.send_message(chat_id=chat_id, text=message)
