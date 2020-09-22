from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api
from datetime import datetime



counter=0
token = "eb6373cdce75509de9eb58904ff7024e91b7dda2c0be392867fb64e7e37e11a3c53bd769b225fec16da9f"
vk = vk_api.VkApi(token=token)
longpoll = VkLongPoll(vk)


for event in longpoll.listen():

    # Если пришло новое сообщение
    if event.type == VkEventType.MESSAGE_NEW:
        

        if event.from_user and not (event.from_me):
            vk.method('messages.send', {'user_id': event.user_id, 'message': 'BRUH', 'random_id': 0})


