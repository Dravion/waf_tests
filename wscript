def options(ctx):
    ctx.load('compiler_c')

def configure(ctx):
    ctx.load('compiler_c')

def build(ctx):
    ctx(features='c cprogram', source='src/main.c', target='hello_world')
