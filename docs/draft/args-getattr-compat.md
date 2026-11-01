# Remaining getattr(args, …) inventory (Task 13)

Scan: `relax/` + `examples/` matching `getattr(args|self.args, "…", default)`.

| Version | sites | unique attrs | vs pre-cleanup (870) |
| --- | ---: | ---: | ---: |
| pre-cleanup `main` | **870** | 376 | 100% |
| after Relax-owned direct-read + Megatron compat (#511–#515 early tip) | ~258 | ~166 | ~29.7% |
| after `optional_arg()` for upstream-optional (#515) | **44** | **31** | **5.1%** |

Cuttable `megatron-or-upstream-optional` call sites now use
`relax.utils.optional_args.optional_arg` (`__dict__.get`) so the
`getattr(..., default)` pattern itself stays rare. Schema-gated CP helpers
live in `relax/backends/megatron/compat.py`.

## Classification legend

| Class | Action |
| --- | --- |
| `sglang-optional` | Keep `getattr` (SGLang parse may be skipped; see slime #1604). |
| `private/runtime marker` | Internal `_…` markers; keep defensive access. |
| `megatron-schema-compat` | Prefer helpers in `relax/backends/megatron/compat.py`. |
| `optional-arg` | Upstream / incomplete Namespace knobs → `optional_arg()`, not `getattr`. |

## Remaining getattr sites by attribute

### sglang-optional (keep)

- `sglang_speculative_algorithm` ×4
- `sglang_enable_deterministic_inference` ×4
- `sglang_config` ×3
- `sglang_dp_size` ×2
- `sglang_profile_num_steps` ×2
- `sglang_sampling_backend` ×2
- `sglang_router_ip` ×1
- `sglang_hf_checkpoint` ×1
- `sglang_external_model_package` ×1
- `sglang_load_format` ×1
- `sglang_pp_size` ×1
- `sglang_enable_hierarchical_cache` ×1
- `sglang_profile_output_dir` ×1
- `sglang_profile` ×1
- `sglang_profile_steps` ×1
- `sglang_profile_step_start` ×1
- `sglang_profile_step_end` ×1
- `sglang_profile_activities` ×1
- `sglang_profile_by_stage` ×1
- `sglang_profile_with_stack` ×1
- `sglang_profile_record_shapes` ×1
- `sglang_rl_on_policy_target` ×1
- `sglang_enable_metrics` ×1

### private/runtime marker (keep)

- `_genrm_colocate_with_rollout` ×2
- `_relax_managed_pd_router_endpoint` ×2
- `_start_rollout_id_explicit` ×1
- `_qwen_fused_head` ×1
- `_relax_resident_sft_actor_verified` ×1
- `_i2i_sft_attempt_id` ×1
- `_relax_shared_expert_gate_ready_verified` ×1
- `_model_source_original_hf_checkpoint` ×1

## By file (remaining getattr only)

- `relax/utils/profile_utils.py` — sglang_profile*
- `relax/distributed/ray/rollout.py` — sglang_* / private markers
- `relax/engine/rollout/sglang_rollout.py` — sglang_*
- `relax/utils/score_centering.py` — sglang_*
- `relax/backends/sglang/arguments.py` — sglang_*
- `relax/utils/arguments.py` — sglang_* / private
- `relax/backends/sglang/sglang_engine.py` — sglang_*
- `relax/distributed/ray/genrm.py` — private markers
- `relax/engine/sft/runtime.py` — private markers
- plus single-site keepers under fsdp/megatron/sglang/model_source/metrics
