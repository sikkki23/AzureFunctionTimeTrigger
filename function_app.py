import logging
import azure.functions as func
import requests

app = func.FunctionApp()

@app.timer_trigger(schedule="10 * * * * *", arg_name="myTimer", run_on_startup=False,
              use_monitor=False) 
def Az_timer_trigger(myTimer: func.TimerRequest) -> None:
    if myTimer.past_due:
        logging.info('The timer is past due!')
    url = "https://jsonplaceholder.typicode.com/posts/1"
    try:
        logging.info('!!!!!!!!!!!!!!!!!!!!!!!!Hello!!!!!!!Python timer trigger function executed.')
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Raises exception for 4XX/5XX errors
        data = response.json()
        logging.info(data)
    except requests.exceptions.RequestException as e:
        logging.info(f"API request failed: {e}")
    