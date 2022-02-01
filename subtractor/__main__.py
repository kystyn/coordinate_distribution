import argparse
from pathlib import Path
from tqdm import tqdm
from PIL import Image, ImageChops
import shutil

def arguments():
    parser = argparse.ArgumentParser(description='Picture subtractor. Subtracts stacked tomographs pictures with specified delta')
    parser.add_argument('--minuend', type=str, help='Address of minuend stack (адрес уменьшаемого стека)')
    parser.add_argument('--subtrahend', type=str, help='Address of subtrahend stack (адрес вычитаемого стека)')
    parser.add_argument('--delta', type=int, help='number in subtrahend stack - number in minuend stack')
    parser.add_argument('--result', type=str, help='Address of result stack')

    args = parser.parse_args()
    return args


def subtract(args):
    # Initialize paths
    minuend: Path = Path(args.minuend)
    if not minuend.is_dir():
        raise RuntimeError('minuend address is invalid')

    subtrahend: Path = Path(args.subtrahend)
    if not subtrahend.is_dir():
        raise RuntimeError('subtrahend address is invalid')

    result: Path = Path(args.result)
    result.mkdir(parents=True, exist_ok=True)

    # Verify stack power equality
    minuend_bmps: list[Path] = list(minuend.glob('*.bmp'))
    minuend_bmps.sort(key=lambda mbmp: int(str(mbmp)[-8:-4]))

    subtrahend_bmps: list[Path] = list(subtrahend.glob('*.bmp'))
    subtrahend_bmps.sort(key=lambda mbmp: int(str(mbmp)[-8:-4]))

    if len(minuend_bmps) != len(subtrahend_bmps):
        raise RuntimeError('minuend power is not equal to subtrahend power')

    start_minuend = 0 if args.delta >= 0 else -args.delta
    start_subtrahend = args.delta if args.delta >= 0 else 0

    # Generate images
    prefix_minuend = minuend_bmps[0].parts[-1][:-8]
    #prefix_subtrahend = subtrahend_bmps[0][:-4]
    start_minuend_abs = int(str(minuend_bmps[0])[-8:-4])
    idx = start_minuend_abs

    for minuend_path, subtrahend_path in\
        tqdm(zip(minuend_bmps[start_minuend:], subtrahend_bmps[start_subtrahend:]),
                    desc='Subtraction progress',
                    total=min(len(minuend_bmps) - start_minuend,
                            len(subtrahend_bmps) - start_subtrahend)):

        minuend_img = Image.open(minuend_path)
        subtrahend_img = Image.open(subtrahend_path)

        if minuend_img.mode != subtrahend_img.mode:
            raise RuntimeError('different image modes')

        if minuend_img.size != subtrahend_img.size:
            raise RuntimeError('different image sizes')

        result_img: Image = ImageChops.subtract(minuend_img, subtrahend_img)
        idx_str = '0' * (4 - len(str(idx))) + str(idx)
        result_img.save(open(f'{args.result}/{prefix_minuend}{idx_str}.bmp', 'wb'))
        idx += 1

    if start_minuend == 0:
        # Copy from minuend end
        for idx in range(-args.delta, 0):
            shutil.copy(str(minuend_bmps[idx]), f'{args.result}/{minuend_bmps[idx].parts[-1]}')
    else:
        # Copy from subtrahend end
        for idx in range(args.delta, 0):
            shutil.copy(str(subtrahend_bmps[idx]), f'{args.result}/{subtrahend_bmps[idx].parts[-1]}')
    


if __name__ == '__main__':
    args = arguments()
    try:
        subtract(args)
    except RuntimeError as e:
        print(f'Error occured: {e}')

