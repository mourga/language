# coding=utf-8
# Copyright 2018 The Google AI Language Team Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Contains custom type definitions."""
from typing import Any, Callable, Dict, Iterable

import jax.numpy as jnp

Array = jnp.ndarray
PRNGKey = jnp.ndarray
Dtype = Any
Shape = Iterable[int]
InitType = Callable[[PRNGKey, Shape, Dtype], Array]
MetricGroups = Dict[str, Dict[str, Array]]
