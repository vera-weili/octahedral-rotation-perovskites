from matplotlib import pyplot as plt
import pandas as pd

def plot_nk():
    plots_df = pd.read_csv("angle_gap", delim_whitespace=True, names=['angle', 'bandgap'])
    print(plots_df.head())
    plots_df.plot(kind='line', x='angle', y='bandgap')
    plt.title("Angle-bandgap correlation")
    plt.xlabel('angle (θ)')
    plt.ylabel('bandgap (eV)')
    plt.savefig('aa')
    #plt.show()

def main():
    plot_nk()

if __name__ == "__main__":
    main()

