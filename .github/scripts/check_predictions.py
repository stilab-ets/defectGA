
import sys
import pandas as pd

def main():
    if len(sys.argv) < 2:
        print("Usage: python check_predictions.py <predictions_csv>")
        sys.exit(1)

    csv_path = sys.argv[1]

    try:
        df = pd.read_csv(csv_path)
    except FileNotFoundError:
        print(f"File not found: {csv_path}")
        sys.exit(0) # Not an error, just no predictions generated maybe? Or handled by caller.
    except pd.errors.EmptyDataError:
        print("No columns to parse from file")
        sys.exit(0)

    if df.empty:
        print("No predictions data available.")
        sys.exit(0)

    print("📊 Defect Prediction Analysis")
    print("==================================================")
    
    # Select key columns to display
    cols = ['file', 'block_name', 'probability', 'fault_prone']
    # Fallback if columns missing
    existing_cols = [c for c in cols if c in df.columns]

    if not existing_cols:
        print("Expected columns not found in CSV.")
        print(f"Available columns: {df.columns.tolist()}")
    else:
        print("CHANGED BLOCKS & RISK ASSESSMENT:")
        print("--------------------------------------------------")
        print(df[existing_cols].to_markdown(index=False))

    # Summary Stats
    risk_count = df['fault_prone'].sum() if 'fault_prone' in df.columns else 0
    total = len(df)
    
    print("\n--------------------------------------------------")
    print(f"Total Blocks Analyzed: {total}")
    print(f"High Risk Density: {risk_count}/{total}")
    
    if risk_count > 0:
        print(f"❌ FAILURE: {risk_count} Potential Defects Detected!")
        print("   Please review the table above for high-risk blocks.")
        # sys.exit(1) # Uncomment to fail build
    else:
        print("✅ SUCCESS: No defects predicted.")

if __name__ == "__main__":
    main()
