import config
import interbellum

bot = interbellum.bot
bot.report('Инициализация...')

from timeit import default_timer as timer

start_time = timer()

from modules.manybotslib import BotsRunner

bots = {
    'Интербеллум': bot
}

runner = BotsRunner(admins=[config.creator], retries=3, show_traceback=True)
runner.add_bots(bots)
runner.set_main_bot(bot, 'status')
bot.report('Готово! Боты запущены и готовы к работе.\nВремени использовано: {} секунд.'.format(timer() - start_time))
runner.run()
