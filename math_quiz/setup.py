from setuptools import setup, find_packages

setup(
    name='math_quiz',
    version='1.0.0',
    description='A simple math quiz game',
    author='Ramisa Bhuiyan Raka',
    author_email='ramisa.bh24@gmail.com',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'math_quiz=math_quiz.math_quiz:math_quiz',
        ],
    },
)
