# Project Configuration
# Using uv for all operations ensures environment consistency
UV = uv

# Directory Structure
BASE_DIRS = app/api app/core app/data/datasets app/data/dataloaders app/data/tokenizers \
            app/data/transforms app/data/preprocessing app/training app/inference \
            app/shared/layers app/shared/activations app/shared/normalization \
            app/shared/attention app/shared/embeddings \
            datasets/raw datasets/processed datasets/external \
            outputs/figures outputs/logs outputs/predictions outputs/benchmarks \
            scripts docs/paper_notes docs/implementation_notes docs/math docs/experiments

PAPERS = attention_is_all_you_need bert gpt vision_transformer swin_transformer \
         flash_attention performer linformer reformer longformer llama template

.PHONY: setup init-dirs sync lint format test check-all clean install-hooks run-hooks

# Full project initialization
setup: sync init-dirs install-hooks
	@echo "Project environment fully configured and pre-commit hooks installed."

# Ensure project dependencies are synced with uv.lock
sync:
	@$(UV) sync

# Define module structures
API_FILES := app/api/routes.py app/api/v1/schemas.py app/api/v1/dependencies.py
CORE_FILES := app/core/config.py app/core/logger.py app/core/utils.py
TRAINING_FILES := app/training/trainer.py app/training/evaluator.py app/training/losses.py \
                  app/training/optimizers.py app/training/schedulers.py app/training/metrics.py \
                  app/training/checkpoint.py
INFERENCE_FILES := app/inference/predictor.py app/inference/decoding.py app/inference/visualization.py

# Consolidated list of all directories to create
DIRS := app/api/v1 app/core app/data/datasets app/data/dataloaders app/data/tokenizers \
        app/data/transforms app/data/preprocessing app/training app/inference \
        app/shared/layers app/shared/activations app/shared/normalization \
        app/shared/attention app/shared/embeddings \
        datasets/raw datasets/processed datasets/external \
        outputs/figures outputs/logs outputs/predictions outputs/benchmarks \
        scripts docs/paper_notes docs/implementation_notes docs/math docs/experiments

init-dirs:
	@echo "Verifying directory structure..."
	# 1. Create all directories and ensure __init__.py exists
	@for dir in $(DIRS); do \
		mkdir -p $$dir && touch $$dir/__init__.py; \
	done
	# 2. Initialize module files
	@touch $(API_FILES) $(CORE_FILES) $(TRAINING_FILES) $(INFERENCE_FILES)
	# 3. Paper scaffold
	@for paper in $(PAPERS); do \
		mkdir -p app/papers/$$paper checkpoints/$$paper notebooks/$$paper; \
		touch app/papers/$$paper/__init__.py; \
		if [ "$$paper" = "template" ] || [ "$$paper" = "attention_is_all_you_need" ]; then \
			mkdir -p app/papers/$$paper/tests && touch app/papers/$$paper/tests/__init__.py; \
		fi; \
	done
	# 4. Root files
	@[ -f README.md ] || touch README.md
	@[ -f .gitignore ] || touch .gitignore
	@[ -f app/main.py ] || touch app/main.py
	@echo "Project architecture initialized with API, Core, and Data modules."

# Pre-commit Hook Management
install-hooks:
	@$(UV) run pre-commit install

run-hooks:
	@$(UV) run pre-commit run --all-files

# Quality Gates
lint:
	@$(UV) run ruff check --fix && uv run ruff format
	@$(UV) run mypy app/

format:
	@$(UV) run ruff format .

test:
	@$(UV) run pytest tests/

check-all: format lint test

# run project server
run-server:
	@$(UV) run uvicorn app.main:app --reload
# Cleanup
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +



# Load variables from .env file
include .env
export

docker-build:
	@docker build --build-arg APP_VERSION=$(API_VERSION) -t $(APP_NAME):$(API_VERSION) .

# Run the container locally, mapping port 8000
docker-run:
	@docker run -it -p 8000:8000 --rm $(APP_NAME):$(API_VERSION)
# Stop and remove all running containers for this image
docker-stop:
	@docker stop $$(docker ps -q --filter ancestor=$(APP_NAME):$(API_VERSION)) 2>/dev/null || true

print-version:
	@echo "Current APP_VERSION is: $(API_VERSION)"
# Remove the local docker image
docker-clean:
	@docker rmi $(APP_NAME):$(API_VERSION) -f