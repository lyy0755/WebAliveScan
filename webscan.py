from lib.common.request import Request
from lib.common.output import Output
from lib.utils.wappalyzer import Wappalyzer
from lib.common.dirbrute import Dirbrute
from lib.utils.tools import *
import fire


class Program(object):
    def __init__(self, target, port, brute):
        output = Output()
        wappalyzer = Wappalyzer()
        request = Request(target, port, output, wappalyzer)
        save_result(request.alive_path, ['url', 'title', 'status', 'size', 'server', 'language', 'application', 'frameworks', 'system'], request.alive_result_list)
        output.resultOutput(f'Alive result save to: {request.alive_path}')
        if brute:
            brute_result_list = []
            output.newLine('')
            for info in request.alive_result_list:
                dirbrute = Dirbrute(info.get('url'), output, brute_result_list)
                dirbrute.run()
            save_result(request.brute_path, ['url', 'status', 'size'], brute_result_list)
            output.resultOutput(f'Brute result save to: {request.brute_path}')


def run(target, port, brute=False):
    main = Program(target, port, brute)


if __name__ == '__main__':
    fire.Fire(run)
