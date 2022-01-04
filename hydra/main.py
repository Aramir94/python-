# pip install --upgrade hydra-core
# https://pjt3591oo.github.io/hydra_translate/build/html/About/GettingStarted.html : docu
import hydra
from hydra.core.config_store import ConfigStore
from config import testConfig


cs = ConfigStore()
cs.store(name="test_config", node=testConfig)
@hydra.main(config_path='conf', config_name="config")
def main(cfg: testConfig):
    print(cfg)
    print(cfg.files)
    print(cfg.params)
    return
main()