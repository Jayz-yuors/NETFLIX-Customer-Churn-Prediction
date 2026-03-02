def compare_models(results_dict):

    print("\n===== MODEL COMPARISON =====")

    for model_name, f1 in results_dict.items():
        print(f"{model_name}: F1 = {f1}")

    best_model = max(results_dict, key=results_dict.get)

    print("\nBest Model:", best_model)

    return best_model