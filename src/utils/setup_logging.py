import yaml
import logging
import logging.config
from pathlib import Path
import os


logging_conf_folder = Path(__file__).parents[1]

with open(os.path.join(logging_conf_folder, 'logging_conf.yaml')) as f:
  log_config = yaml.safe_load(f.read())
  logging.config.dictConfig(log_config)

logger = logging.getLogger('dev')