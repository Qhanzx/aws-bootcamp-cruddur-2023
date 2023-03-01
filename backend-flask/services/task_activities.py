from datetime import datetime, timedelta, timezone
from aws_xray_sdk.core import xray_recorder

class TaskActivities:
  def run():
    now = datetime.now(timezone.utc).astimezone()
    results = [{
        'uuid': '68f126b0-1ceb-4a33-88be-d90fa7109eee',
        'handle':  'MMA Mark',
        'message': 'This is my freeium version!',
        'created_at': (now - timedelta(days=2)).isoformat(),
        'expires_at': (now + timedelta(days=5)).isoformat(),
        'likes_count': 5,
        'replies_count': 1,
        'reposts_count': 0,
        'replies': [{
            'uuid': '26e12864-1c26-5c3a-9658-97a10f8fea67',
            'reply_to_activity_uuid': '68f126b0-1ceb-4a33-88be-d90fa7109eee',
            'handle':  'Shane',
            'message': 'This post has no honor!',
            'likes_count': 0,
            'replies_count': 4,
            'reposts_count': 90,
            'created_at': (now - timedelta(days=2)).isoformat()
        }],
    }
    ]
    dict = {
          'now': now.isoformat(),
          'result-size': len(results)

      }

    # Start a segment
    segment = xray_recorder.begin_segment('task_activities')
    # Add metadata or annotation here if necessary
    segment.put_metadata('key', dict, 'namespace')
    return results
