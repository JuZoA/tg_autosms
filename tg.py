from telethon.sync import TelegramClient
from telethon.tl.functions.messages import SendMessageRequest
import time
from telethon import errors
import asyncio
# Вставьте ваши данные авторизации
api_id = ''
api_hash = ''
phone_number = ''

# Создаем экземпляр клиента Telegram
client = TelegramClient('session_name', api_id, api_hash)

# Функция для отправки сообщения в чат
async def send_message(chat_id, message):
    await client.send_message(chat_id, message)

# Основной цикл программы
async def main():
    k = 1
    async with client:
        while True:
            try:
                chat_ids = []  # вставьте сюда айди нужных чатов
                message = """"""
                for chat_id in chat_ids:
                    try:
                        await send_message(chat_id, message)
                        print(f'сообщение {k} доставлено! ')
                        k+=1
                        await asyncio.sleep(45)
                    except errors.FloodWaitError as e:
                        # Обработка ошибки FloodWaitError
                        print(f"Пауза в {e.seconds} секунд")
                        await asyncio.sleep(e.seconds)
                        continue
                
                # Пауза в 50 секунд перед началом следующего цикла
                await asyncio.sleep(50)

            except Exception as e:
                # Обработка возможных ошибок
                print(e)

# Запуск основного цикла программы
asyncio.run(main())
