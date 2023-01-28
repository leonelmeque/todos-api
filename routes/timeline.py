from flask import jsonify, Blueprint, request
from models.timelines import timelines

timeline_routes = Blueprint('timeline', __name__)


@timeline_routes.get('/timeline/<string:id>')
def get_timeline(id):
    try:
        result = [timeline for timeline in timelines if timeline["id"] == id]
        if (len(result) > 0):
            return jsonify({"result": result[0]})
        return jsonify({"message": "No timeline was found", result: []})
    except Exception as e:
        print(e)
        return jsonify({"message": "Something went wrong"})


@timeline_routes.get('/timeline/<string:id>/<string:event_id>')
def get_timeline_event(id, event_id):
    result = [timeline for timeline in timelines if timeline["id"] == id]
    if (len(result) > 0):
        event_result = [event for event in result[0]
                        if event["id"] == event_id]
        if (len(event_result) > 0):
            return jsonify({"result": event_result[0]})
        return jsonify({"message": "Event not found", "result": []})


@timeline_routes.post('/timeline')
def add_timeline():
    try:
        id = request.json['id'],
        events = request.json['events']

        timelines.insert(0, {
            "id": id,
            "events": events
        })

        return jsonify({"message": "New timeline was created", "results": []})
    except Exception as e:
        print(e)
        return jsonify({"message": "Something went wrong"})


@timeline_routes.post('/timeline/<string:id>/')
def add_timeline_event(id):
    try:
        index = [timeline for timeline in timelines if timeline["id"] == id]

        if (len(index) <= 0):
            return jsonify({"message": "Timeline was not found"})

        timelines[index[0]]["events"].insert({
            "id": request.json['id'],
            "creator": request.json['creator'],
            "date": request.json["date"],
            "time": request.json["time"],
            "title": request.json["title"],
            "description": request.json["description"],
            "assigned": request.json["assigned"]
        })

        return jsonify({"message": "Event was added succesfuly"})
    except:
        return jsonify({"message": "An error has occured"})
