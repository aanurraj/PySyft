# stdlib
from typing import Dict
from typing import Union

allowlist: Dict[str, Union[str, Dict[str, str]]] = {}  # (path: str, return_type:type)

# MNIST
allowlist["torchvision.transforms.Compose"] = "torchvision.transforms.Compose"
# TODO: Compose.transforms property only exists on the object not on the class?
# allowlist["torchvision.transforms.Compose.transforms"] = "syft.lib.python.list.List"
allowlist["torchvision.transforms.ToTensor"] = "torchvision.transforms.ToTensor"
allowlist["torchvision.transforms.Normalize"] = "torchvision.transforms.Normalize"
# TODO: Normalize properties only exists on the object not on the class?
# allowlist["torchvision.transforms.Normalize.inplace"] = "syft.lib.python.bool.Bool"
# TODO: mean and std are actually tuples
# allowlist["torchvision.transforms.Normalize.mean"] = "syft.lib.python.list.List"
# allowlist["torchvision.transforms.Normalize.std"] = "syft.lib.python.list.List"

allowlist["torchvision.datasets.MNIST"] = "torchvision.datasets.MNIST"