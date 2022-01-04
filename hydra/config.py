# hydra config datatype
# config definition

from dataclasses import dataclass

@dataclass
class Files:
    train_data: str
    test_data: str

@dataclass
class Params:
  epoch_count: int
  lr: float
  batch_size: int

@dataclass
class testConfig:
    files: Files
    params: Params