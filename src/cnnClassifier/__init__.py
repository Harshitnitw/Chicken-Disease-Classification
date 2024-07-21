import os, sys, logging, pytz
from datetime import datetime

logging_str="[%(asctime)s] %(filename)s:%(lineno)s %(module)s:%(funcName)s() %(name)s - %(levelname)s - %(message)s"

timezone_ind= pytz.timezone('Asia/Kolkata')

ist_local = datetime.now(timezone_ind)


LOG_FILE=f"{ist_local.strftime('%d_%m_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs")
os.makedirs(logs_path,exist_ok=True)


LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(LOG_FILE_PATH)
    ]
)

logger=logging.getLogger("cnnClassifierLogger")