from fastapi import Depends, HTTPException
from models.user import UserModel
from models.history import HistoryModel
from schemas.historySchema import HistoryCreate
from database import getDatabase
from sqlalchemy.orm import Session


class HistoryController:
    @staticmethod
    def createHistory(history: HistoryCreate, db: Session):
        newHistory = HistoryModel(
            # user_id = request.user_id,
            user_id = history.user_id,
            song_id = history.song_id,
            play_date = history.play_date
        )
        db.add(newHistory)
        db.commit()
        db.refresh(newHistory)
        return newHistory
    
    def getHistoryById(historyId: int, db: Session = Depends(getDatabase)):
        return db.query(HistoryModel).filter(HistoryModel.id == historyId).first()

    # def updateHistory(historyId: int, History: HistoryUpdate, db: Session):
    #     dbHistoryId = db.query(HistoryModel).filter(HistoryModel.id == historyId).first()

    #     if History.name is not None:
    #         dbHistoryId.name = History.name
    #     else:
    #         raise HTTPException(status_code=400, detail="Invalid name")

    #     db.commit()
    #     return {"msg": "Updated"}
    
    def deleteHistory(historyId: int, db: Session):
        dbHistoryId = db.query(HistoryModel).filter(HistoryModel.id == historyId).first()
        db.delete(dbHistoryId)
        db.commit()
        return {"msg": "Deleted"}
    