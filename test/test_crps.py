# SPDX-FileCopyrightText: Copyright (c) 2023 NVIDIA CORPORATION & AFFILIATES.
# SPDX-FileCopyrightText: All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import numpy as np
import properscoring
import torch

from earth2mip.crps import kcrps


def test_crps_cdf():
    n = 10
    x = torch.randn((10, n))
    y = torch.randn((n,))
    out = kcrps(x, y, dim=0)
    reference = properscoring.crps_ensemble(y.numpy(), x.numpy(), axis=0)
    np.testing.assert_allclose(out.numpy(), reference, rtol=1e-6)
