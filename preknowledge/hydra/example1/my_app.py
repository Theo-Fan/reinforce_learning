from omegaconf import DictConfig, OmegaConf
import hydra 


@hydra.main(version_base=None, config_path=".", config_name="config")
def my_app(cfg: DictConfig) -> None:
    print(cfg.db.user)
    print(OmegaConf.to_yaml(cfg))

if __name__ == "__main__":
    my_app()
