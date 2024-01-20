import keyboard
import time
import random

def main():
    # consecutive_presses_required = 3
    # # consecutive_presses = 0

    # while True:
    #     for i in range(consecutive_presses_required - 1):
    #         key_event = keyboard.read_event(suppress=True)
    #     key_event = keyboard.read_event(suppress=False)
        # time.sleep(0.5)
    
    # x = random.randint(2, 6)
    # print(x)
    # consecutive_presses_required = x
    # # consecutive_presses = 0

    # while True:
    #     cnt = 0
    #     while (cnt < consecutive_presses_required - 1):
    #         print(consecutive_presses_required)
    #         key_event = keyboard.read_event(suppress=True)
    #         if(key_event.event_type == keyboard.KEY_DOWN):
    #             cnt += 1
        
    #     key_event = keyboard.read_event(suppress=False)
    #     while(key_event.event_type != keyboard.KEY_DOWN):
    #         key_event = keyboard.read_event(suppress=False)


    x = random.randint(2, 6)
    print(x)
    consecutive_presses_required = x

    while True:
        cnt = 0
        while cnt < consecutive_presses_required - 1:
            key_event = keyboard.read_event(suppress=True)
            if key_event.event_type == keyboard.KEY_DOWN and key_event.name.isalnum():
                # if key_event.name in ['shift', 'caps lock']:
                #     # Handle Shift and Caps Lock separately if needed
                #     pass
                # else:
                cnt += 1
            if key_event.event_type == keyboard.KEY_UP and key_event.name in ['shift', 'caps lock']:
                keyboard.release(key_event.name)

            if key_event.event_type == keyboard.KEY_DOWN and key_event.name in ['shift', 'caps lock']:
                keyboard.press(key_event.name)
            

        key_event = keyboard.read_event(suppress=False)
        # while key_event.event_type != keyboard.KEY_DOWN or key_event.name in ['shift', 'caps lock']:
        while key_event.event_type != keyboard.KEY_DOWN and key_event.name.isalnum():
            key_event = keyboard.read_event(suppress=False)
            x = random.randint(2, 6)
            print(x)
            consecutive_presses_required = x


        # Now you can use key_event.name or key_event.event_type as needed
        # if key_event.name not in ['shift', 'caps lock']:
        #     # Adjust the case of the character if needed
        #     character = key_event.name.upper() if 'shift' in keyboard._pressed_events else key_event.name.lower()
        #     print(character)
     

    
    # while True:
    #     try:
    #         key = key_event.name
    #         print(key)

    #         pressed = False
    #         if key_event.event_type == keyboard.KEY_UP:
    #             key_event = keyboard.read_event(suppress=True)
    #             print("up")
    #             pressed = False

    #         if key_event.event_type == keyboard.KEY_DOWN and not pressed:
    #             pressed = True
    #             consecutive_presses += 1
    #             if(consecutive_presses == consecutive_presses_required - 1):
    #                 key_event = keyboard.read_event(suppress=False)
    #             if(consecutive_presses == consecutive_presses_required):
    #                 key_event = keyboard.read_event(suppress=True)
    #                 consecutive_presses = 0
                
    #     except KeyboardInterrupt:
    #         break

if __name__ == "__main__":
    main()
