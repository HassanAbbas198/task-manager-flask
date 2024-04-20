from flask import Blueprint
from . import controllers

task_bp = Blueprint('task', __name__)
