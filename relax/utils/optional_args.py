# Copyright (c) 2026 Relax Authors. All Rights Reserved.

"""Optional Namespace field access without ``getattr(..., default)``.

Task 13 wants Relax-owned fields read as ``args.xxx`` after parse. Upstream-
optional / incomplete test Namespaces still need a defensive read; centralize
that here so the ``getattr(args, "name", default)`` pattern can stay rare
(sglang-optional and private markers only).
"""

from __future__ import annotations

from typing import Any, TypeVar


T = TypeVar("T")


def optional_arg(args: Any, name: str, default: T = None) -> T | Any:
    """Return ``args.name`` when the attribute exists, otherwise ``default``.

    Uses ``__dict__`` lookup so call sites do not reintroduce
    ``getattr(args, name, default)``. Prefer direct ``args.name`` for fields
    that parse/validate always assign.
    """
    mapping = args.__dict__ if hasattr(args, "__dict__") else None
    if isinstance(mapping, dict):
        return mapping.get(name, default)
    return default
