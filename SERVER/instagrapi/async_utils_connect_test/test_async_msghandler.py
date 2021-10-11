import time
import asyncio
import os

from instagrapi import Client

# from utils.get_client import *
# from utils.download_image_from_DM import *
# from utils.detect_images import *
# from utils.send_DM import *
from utils.get_request_from_DM import * # local Utils function import


cl = Client()
cl.login('osam_testbot','admin0408!')
messages = [] 

async def check_unread(messages):
    while True: 
        await asyncio.sleep(1) # 1초 interval로 Thread 읽어옴
        unread_threads = cl.direct_threads(20,'unread')
        unread_len = len(unread_threads)
        print(f'unread msgs remaining : {unread_len}')
        if unread_len > 0:
            for idx in range(unread_len):
                msg = unread_threads[idx].messages[0].text
                user_id = unread_threads[idx].messages[0].user_id # 메세지 전송한 user의 id 추출
                thread_id = unread_threads[idx].id # thread ID 추출
                cl.direct_answer(thread_id,'msg received')
                print(msg) # 사용자의 msg 출력
                messages.append((msg,user_id,thread_id)) # messages list에 msg와 thread_id 를 추가

# messages를 읽어온 후 가장 최신의 msg부터 각자 handling 한다.(concurrently라는 가정 하)
async def msg_handler(messages):
    while True:
        if messages:
            print(messages)
            print('Msg READ')
            # 읽은 msgs는 삭제 처리
            msg_data = messages.pop(0)

            msg = msg_data[0]
            user_id = msg_data[1]
            thread_id = msg_data[2]

            print(f'input message : {msg_data}')
            
            if msg == 'Test':
                print('Test Route')
                await Test_img_process(msg)
            elif msg == '도움':
                print('Help Route')
                # thread_id = msg_data[1] # Thread_id 의 idx : 1
                await send_help(cl,user_id) # cl = Client Pass
            elif msg == '게시물 전체 검사':
                print('Post Check Route')
                await read_all_posts(cl,user_id)
            # elif msg == '게시물 검사':
            #     await post_check(cl,user_id,thread_id)
            else:
                print('Invalid Command Route')
                await send_invalid(cl,user_id)
                

        else:
            print('no messages left')
            await asyncio.sleep(1)

async def Test_img_process(msg):
    await asyncio.sleep(3) # img processing 예상 소요시간 임의 설정
    print(f'{msg} : img_processing done')

# main 실행 함수
async def main(messages) :
    await asyncio.gather(
        check_unread(messages),
        msg_handler(messages), # 하나의 함수당 Thread 1로 작동하는 개념 (동시에 하나의 명령씩 수행 가능)
        # msg_handler(messages),
        # msg_handler(messages),
    )
    
if __name__ == "__main__":
    asyncio.run(main(messages))

# print(f"stated at {time.strftime('%X')}")
# asyncio.run(main(messages))
# print(f"finish at {time.strftime('%X')}")