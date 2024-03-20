'''Alarm Clock: Design an alarm clock application that allows users to set alarms with specific
 times and messages. It can play a sound or display a message when the alarm goes off.'''

import streamlit as st
import datetime
import time

# Defining Function to set an alarm
def set_alarm(alarm_time, alarm_message):
    while True:
        # Getting current time
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        # Checking if current time matches the alarm time
        if current_time == alarm_time:
            st.write(f"ALARM: {alarm_message}")
            break
        # Wait for 1 second before checking again
        time.sleep(1)

# Defining Main function for Streamlit app
def main():
    st.title("Alarm Clock")

    # Alarm input fields
    alarm_time = st.time_input("Set alarm time:")
    alarm_message = st.text_input("Set alarm message:")

    # Set alarm button
    if st.button("Set Alarm"):
        alarm_time_str = alarm_time.strftime("%H:%M:%S")
        st.write(f"Alarm set for {alarm_time_str}")

        # Start the alarm in a separate thread
        set_alarm(alarm_time_str, alarm_message)

if __name__ == "__main__":
    main()
