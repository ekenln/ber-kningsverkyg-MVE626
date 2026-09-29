import matplotlib.pyplot as plot

def plot_function(filename:str):
    try:
        f = open(filename)
        try:
            x_list = f.readline().split(', ')
            y_list = f.readline().split(', ')
            try:
                x_list = list(map(float, x_list))
                y_list = list(map(float, y_list))
                try:
                    plot.plot(x_list, y_list)
                    try:
                        plot.savefig(f'{filename}_plot.png')
                        print('OK')
                        f.close()
                        return 'OK'
                    except:
                        print('Fel vid lagring av bild')
                        return 'Fel vid lagring av bild'
                except:
                    return 'Fel vid plottning'
            except:
                print('Fel vid omvandling till flyttal')
                return 'Fel vid omvandling till flyttal'
        except:
            print('Fel vid inläsning')
            return 'Fel vid inläsning'
    except:
        print('Fel vid öppning av filen')
        return 'Fel vid öppning av filen'

from pathlib import Path

base_dir = Path(__file__).parent

file_path1 = base_dir / 'Missplot1.txt'
file_path2 = base_dir / 'Missplot2.txt'
file_path3 = base_dir / 'Missplot3.txt'
file_path4 = base_dir / 'Missplot4.txt'
file_path5 = base_dir / 'Testplot.txt'

plot_function(file_path5)