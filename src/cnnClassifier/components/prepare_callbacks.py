import os,pytz
import urllib.request as request
import zipfile
import tensorflow as tf
import time
from datetime import datetime
from cnnClassifier.entity.config_entity import PrepareCallbacksConfig

class PrepareCallback:
    def __init__(self,config:PrepareCallbacksConfig):
        self.config=config
    
    @property
    def _create_tf_callbacks(self):
        timezone_ind= pytz.timezone('Asia/Kolkata')
        ist_local = datetime.now(timezone_ind)
        timestamp=ist_local.strftime('%d_%m_%Y_%H_%M_%S')
        tb_running_log_dir=os.path.join(
            self.config.tensorboard_root_log_dir,
            f"tb_logs_at_{timestamp}"
        )
        return tf.keras.callbacks.TensorBoard(log_dir=tb_running_log_dir)
    
    @property
    def _create_ckpt_callbacks(self):
        return tf.keras.callbacks.ModelCheckpoint(
            filepath=self.config.checkpoint_model_filepath,
            save_best_only=True
        )
    
    def get_tb_ckpt_callback(self):
        return [
            self._create_tf_callbacks,
            self._create_ckpt_callbacks
        ]
